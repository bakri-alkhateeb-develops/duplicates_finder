import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from helpers import find_duplicates, get_file_size
from datetime import datetime


def write_results_to_file(duplicates, output_file):
    """Write duplicate files to a text file."""
    with open(output_file, "w", encoding="utf-8") as f:
        if not duplicates:
            f.write("No duplicate files found.\n")
            return

        total_groups = len(duplicates)
        total_files = sum(len(files) for files in duplicates.values())
        total_wasted_space = 0

        f.write("=" * 80 + "\n")
        f.write("DUPLICATE FILES REPORT\n")
        f.write("=" * 80 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(
            f"\nFound {total_groups} duplicate group(s) with {total_files} total files.\n\n"
        )

        for group_num, (hash_val, files) in enumerate(duplicates.items(), 1):
            file_size = os.path.getsize(files[0])
            wasted_space = file_size * (len(files) - 1)
            total_wasted_space += wasted_space

            f.write("-" * 80 + "\n")
            f.write(
                f"Group {group_num}: {len(files)} duplicate files ({get_file_size(files[0])} each)\n"
            )
            f.write("-" * 80 + "\n")

            for idx, file_path in enumerate(files, 1):
                f.write(f"  [{idx}] {file_path}\n")

            f.write("\n")

        wasted_display = total_wasted_space
        for unit in ["B", "KB", "MB", "GB"]:
            if wasted_display < 1024.0:
                wasted_str = f"{wasted_display:.2f} {unit}"
                break
            wasted_display /= 1024.0
        else:
            wasted_str = f"{wasted_display:.2f} TB"

        f.write("=" * 80 + "\n")
        f.write(f"Potential space savings: {wasted_str}\n")
        f.write("=" * 80 + "\n")


def create_progress_dialog(folder_path):
    """Create and return a progress dialog window."""
    progress_window = tk.Tk()
    progress_window.title("Scanning for Duplicates")
    progress_window.geometry("450x150")
    progress_window.resizable(False, False)
    progress_window.attributes("-topmost", True)

    progress_window.update_idletasks()
    x = (progress_window.winfo_screenwidth() // 2) - (450 // 2)
    y = (progress_window.winfo_screenheight() // 2) - (150 // 2)
    progress_window.geometry(f"450x150+{x}+{y}")

    frame = ttk.Frame(progress_window, padding="20")
    frame.pack(fill=tk.BOTH, expand=True)

    display_path = folder_path if len(folder_path) <= 50 else "..." + folder_path[-47:]
    folder_label = ttk.Label(frame, text=f"Scanning: {display_path}")
    folder_label.pack(pady=(0, 10))

    status_label = ttk.Label(frame, text="Initializing...")
    status_label.pack(pady=(0, 10))

    progress_bar = ttk.Progressbar(frame, mode="determinate", length=400, maximum=100)
    progress_bar.pack()

    progress_window.deiconify()
    progress_window.lift()
    progress_window.focus_force()
    progress_window.update_idletasks()
    progress_window.update()

    return progress_window, status_label, progress_bar


def main():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="Select folder to scan for duplicates")

    if not folder_path:
        messagebox.showinfo("Cancelled", "No folder selected. Exiting.")
        root.destroy()
        return

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path. Exiting.")
        root.destroy()
        return

    progress_window, status_label, progress_bar = create_progress_dialog(folder_path)

    progress_window.update_idletasks()
    progress_window.update()

    def show_progress(current, total):
        if total > 0:
            percent = (current / total) * 100
            progress_bar["value"] = percent
            status_label.config(
                text=f"Processing: {current}/{total} files ({percent:.1f}%)"
            )
        progress_window.update_idletasks()
        progress_window.update()

    duplicates = find_duplicates(folder_path, show_progress)

    progress_window.destroy()
    root.update()

    output_file = "duplicates_report.txt"
    write_results_to_file(duplicates, output_file)

    total_groups = len(duplicates) if duplicates else 0
    messagebox.showinfo(
        "Scan Complete",
        f"Found {total_groups} duplicate group(s).\n\n"
        f"Results saved to:\n{os.path.abspath(output_file)}",
    )

    root.destroy()


if __name__ == "__main__":
    main()
