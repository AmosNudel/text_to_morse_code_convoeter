import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import tkinter.font as tkfont

# ASCII art for the program
ASCII_ART = """

8b    d8  dP"Yb  88""Yb .dP"Y8 888888      dP""b8  dP"Yb  8888b.  888888      dP""b8  dP"Yb  88b 88 Yb    dP 888888 88""Yb 888888 888888 88""Yb 
88b  d88 dP   Yb 88__dP `Ybo." 88__       dP   `" dP   Yb  8I  Yb 88__       dP   `" dP   Yb 88Yb88  Yb  dP  88__   88__dP   88   88__   88__dP 
88YbdP88 Yb   dP 88"Yb  o.`Y8b 88""       Yb      Yb   dP  8I  dY 88""       Yb      Yb   dP 88 Y88   YbdP   88""   88"Yb    88   88""   88"Yb  
88 YY 88  YbodP  88  Yb 8bodP' 888888      YboodP  YbodP  8888Y"  888888      YboodP  YbodP  88  Y8    YP    888888 88  Yb   88   888888 88  Yb 

"""

# Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '@': '.--.-.'
}

# Color scheme
COLORS = {
    'bg': '#E3F2FD',  # Light blue
    'fg': '#2C3E50',  # Dark blue-gray
    'accent': '#3498DB',  # Blue
    'button': '#34495E',  # Dark gray
    'success': '#27AE60',  # Green
    'error': '#E74C3C',  # Red
    'button_text': '#AED6F1',  # Light blue for button text
    'text_field': '#FFFFFF'  # White for text fields
}

def validate_input(text):
    """
    Validates if the input contains only valid characters for Morse code conversion.
    Returns the validated string or raises an exception.
    """
    try:
        # Check if input is empty
        if not text.strip():
            raise ValueError("Input cannot be empty")
        
        # Check if input contains only valid characters
        valid_chars = set(MORSE_CODE.keys())
        if not all(char.upper() in valid_chars for char in text):
            raise ValueError("Input contains invalid characters. Only letters, numbers, and basic punctuation are allowed.")
        
        return text
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def convert_to_morse(text):
    """
    Converts the input text to Morse code.
    """
    try:
        # Convert text to uppercase and convert each character to Morse code
        morse_text = ' '.join(MORSE_CODE[char.upper()] for char in text)
        return morse_text
    except Exception as e:
        messagebox.showerror("Error", f"Error during conversion: {str(e)}")
        return None

class MorseCodeConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Morse Code Converter")
        self.root.geometry("900x700")
        self.root.configure(bg=COLORS['bg'])
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('default')  # Reset to default theme
        
        # Configure frame styles
        self.style.configure('TFrame', background=COLORS['bg'])
        self.style.configure('TLabelframe', background=COLORS['bg'], foreground=COLORS['fg'])
        self.style.configure('TLabelframe.Label', background=COLORS['bg'], foreground=COLORS['fg'], font=('Helvetica', 10, 'bold'))
        
        # Configure button styles
        self.style.configure('TButton',
                           font=('Helvetica', 10),
                           padding=10)
        
        # Create a custom button style
        self.style.configure('Custom.TButton',
                           background=COLORS['button'],
                           foreground=COLORS['button_text'])
        
        self.style.map('Custom.TButton',
                      background=[('active', COLORS['accent']), ('!active', COLORS['button'])],
                      foreground=[('active', COLORS['button_text']), ('!active', COLORS['button_text'])])
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20", style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # ASCII Art Label
        ascii_font = tkfont.Font(family='Courier', size=8)
        ascii_label = ttk.Label(main_frame, 
                              text=ASCII_ART,
                              font=ascii_font,
                              foreground=COLORS['accent'],
                              background=COLORS['bg'])
        ascii_label.pack(pady=10)
        
        # Title Label
        title_font = tkfont.Font(family='Helvetica', size=16, weight='bold')
        title_label = ttk.Label(main_frame,
                              text="Morse Code Converter",
                              font=title_font,
                              foreground=COLORS['fg'],
                              background=COLORS['bg'])
        title_label.pack(pady=(0, 20))
        
        # Input Frame
        input_frame = ttk.LabelFrame(main_frame, text="Input Text", padding="10")
        input_frame.pack(fill=tk.X, pady=5)
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            height=5,
            wrap=tk.WORD,
            font=('Helvetica', 11),
            bg='#34495E',
            fg=COLORS['text_field'],
            insertbackground=COLORS['text_field']
        )
        self.input_text.pack(fill=tk.X, expand=True)
        
        # Buttons Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=15)
        
        convert_btn = ttk.Button(button_frame,
                               text="Convert to Morse Code",
                               command=self.convert_text,
                               style='Custom.TButton')
        convert_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = ttk.Button(button_frame,
                             text="Clear All",
                             command=self.clear_text,
                             style='Custom.TButton')
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Output Frame
        output_frame = ttk.LabelFrame(main_frame, text="Morse Code Output", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=10,
            wrap=tk.WORD,
            font=('Courier', 12),
            bg='#34495E',
            fg=COLORS['text_field'],
            insertbackground=COLORS['text_field']
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame,
                             textvariable=self.status_var,
                             relief=tk.SUNKEN,
                             anchor=tk.W,
                             padding=(5, 2),
                             background=COLORS['bg'],
                             foreground=COLORS['fg'])
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))
    
    def convert_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        validated_text = validate_input(text)
        if validated_text:
            morse_result = convert_to_morse(validated_text)
            if morse_result:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert("1.0", morse_result)
                self.status_var.set("✓ Conversion successful")
    
    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.status_var.set("Text cleared")

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeConverter(root)
    root.mainloop()
