import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.tracker import Tracker

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Package Tracker")
        self.setup_ui()

    def setup_ui(self):
        self.label = ttk.Label(self.root, text="Enter Tracking Numbers (comma separated):")
        self.label.pack(padx=10, pady=5)

        self.tracking_entry = ttk.Entry(self.root, width=50)
        self.tracking_entry.pack(padx=10, pady=5)

        self.track_button = ttk.Button(self.root, text="Track", command=self.track_packages)
        self.track_button.pack(padx=10, pady=5)

        self.results_text = tk.Text(self.root, height=10, width=60)
        self.results_text.pack(padx=10, pady=5)

        self.tracker = Tracker()

    def track_packages(self):
        tracking_numbers = [num.strip() for num in self.tracking_entry.get().split(',')]
        print(f"Tracking Numbers: {tracking_numbers}")  # Debugging line
        carrier_codes = {num: 1151 for num in tracking_numbers}  # Example carrier code; adjust as needed
        try:
            response = self.tracker.get_tracking_info(tracking_numbers, carrier_codes)
            print(f"API Response: {response}")  # Debugging line
            self.display_results(response)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


    def display_results(self, response):
        print(f"Displaying Results: {response}")  # Debugging line
        self.results_text.delete(1.0, tk.END)
        for item in response.get('data', {}).get('accepted', []):
            tracking_number = item['number']
            carrier_name = self.tracker.get_carrier_name(item['carrier'])
            status = item['track_info']['latest_status']['status']
            self.results_text.insert(tk.END, f"Tracking Number: {tracking_number}\n")
            self.results_text.insert(tk.END, f"Carrier: {carrier_name}\n")
            self.results_text.insert(tk.END, f"Status: {status}\n\n")
