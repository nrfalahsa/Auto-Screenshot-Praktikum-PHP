"""
AUTO SCREENSHOT PHP - VSCode + Brave (Laragon)
Jalankan: python auto_screenshot_php.py
Requirement: pip install pyautogui pillow pywin32
"""

import os
import time
import subprocess
import glob
import ctypes
import pyautogui
import win32gui
import win32con
import win32process
import win32api

# ============================================================
#  KONFIGURASI - SESUAIKAN INI
# ============================================================
PHP_FOLDER      = r"C:\laragon\www\praktikum"  # Folder project PHP kamu
OUTPUT_FOLDER   = r"C:\laragon\www\Praktikum"           # Folder hasil screenshot
LOCALHOST_BASE  = "http://localhost/Praktikum"  # URL base di Laragon (ubah jika beda)
BRAVE_EXE       = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" # Path ke Brave, sesuaikan jika beda
DELAY_BROWSER   = 1    # Detik tunggu browser load (naikkan jika lambat)
DELAY_VSCODE    = 1    # Detik tunggu VSCode buka file
# ============================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
screen_w, screen_h = pyautogui.size()
half_w = screen_w // 2

print(f"\n{'='*50}")
print(f"  AUTO SCREENSHOT PHP")
print(f"  Resolusi: {screen_w}x{screen_h}")
print(f"  Output  : {OUTPUT_FOLDER}")
print(f"{'='*50}\n")


def find_window_by_title(title_part):
    """Cari handle window berdasarkan sebagian judul."""
    result = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title_part.lower() in title.lower():
                result.append(hwnd)
    win32gui.EnumWindows(callback, None)
    return result[0] if result else None


def force_foreground(hwnd):
    """Paksa window ke depan - workaround untuk Windows 10/11."""
    try:
        win32gui.SetForegroundWindow(hwnd)
    except Exception:
        try:
            fg = win32gui.GetForegroundWindow()
            if fg:
                fg_thread = win32process.GetWindowThreadProcessId(fg)[0]
                cur_thread = ctypes.windll.kernel32.GetCurrentThreadId()
                ctypes.windll.user32.AttachThreadInput(fg_thread, cur_thread, True)
                win32gui.SetForegroundWindow(hwnd)
                ctypes.windll.user32.AttachThreadInput(fg_thread, cur_thread, False)
        except Exception:
            try:
                pyautogui.press('alt')
                time.sleep(0.1)
                win32gui.SetForegroundWindow(hwnd)
            except Exception:
                pass  # Lanjut saja meski gagal set foreground


def move_window(hwnd, x, y, w, h):
    """Pindahkan & resize window, tangani semua error."""
    if not hwnd:
        return
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.MoveWindow(hwnd, x, y, w, h, True)
        force_foreground(hwnd)
    except Exception as e:
        print(f"  [!] Gagal atur posisi window (dilanjutkan): {e}")


def take_screenshot(save_path):
    """Ambil screenshot full screen dan simpan."""
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)


# Cari semua file PHP
php_files = sorted(glob.glob(os.path.join(PHP_FOLDER, "**", "*.php"), recursive=True))
total = len(php_files)

if total == 0:
    print(f"[ERROR] Tidak ada file PHP ditemukan di: {PHP_FOLDER}")
    input("Tekan Enter untuk keluar...")
    exit()

print(f"Ditemukan {total} file PHP\n")

for counter, filepath in enumerate(php_files, start=1):
    filename       = os.path.basename(filepath)
    filename_noext = os.path.splitext(filename)[0]

    relative_path = os.path.relpath(filepath, PHP_FOLDER).replace("\\", "/")
    url = f"{LOCALHOST_BASE}/{relative_path}"

    print(f"[{counter}/{total}] {filename}")
    print(f"         URL: {url}")

    # --- Buka file di VSCode ---
    subprocess.Popen(["code", filepath], shell=True)
    time.sleep(DELAY_VSCODE)

    # --- Buka URL di Brave ---
    subprocess.Popen([BRAVE_EXE, url])
    time.sleep(DELAY_BROWSER)

    # --- Atur posisi VSCode di KIRI ---
    # Offset -4 dan lebar +8 untuk nutup border/shadow window Windows
    vscode_hwnd = find_window_by_title("Visual Studio Code")
    if vscode_hwnd:
        move_window(vscode_hwnd, -4, 1, half_w + 12, screen_h)
    else:
        print("  [!] VSCode window tidak ditemukan")

    time.sleep(2)

    # --- Atur posisi Brave di KANAN ---
    # Mulai dari half_w - 4 agar tidak ada celah, lebar +8 untuk nutup border kanan
    brave_hwnd = find_window_by_title("Brave")
    if not brave_hwnd:
        brave_hwnd = find_window_by_title(filename)
    if brave_hwnd:
        move_window(brave_hwnd, half_w - 4, 4, half_w + 15, screen_h)
    else:
        print("  [!] Brave window tidak ditemukan")

    time.sleep(2)

    # --- Ambil screenshot ---
    safe_name       = "".join(c if c.isalnum() or c in "._- " else "_" for c in filename_noext)
    screenshot_path = os.path.join(OUTPUT_FOLDER, f"{counter:03d}_{safe_name}.png")
    take_screenshot(screenshot_path)
    print(f"  Tersimpan: {screenshot_path}\n")

    time.sleep(0.3)

print(f"\n{'='*50}")
print(f"  SELESAI! {total} screenshot tersimpan")
print(f"  Lokasi: {OUTPUT_FOLDER}")
print(f"{'='*50}\n")

os.startfile(OUTPUT_FOLDER)
input("Tekan Enter untuk keluar...")