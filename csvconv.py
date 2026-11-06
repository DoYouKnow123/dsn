import csv
from pathlib import Path

def convert_csv_dir_to_txt(input_dir_path: str, output_file_path: str):
    """
    Combines all CSV files in a directory into a single formatted text file.
    """
    input_dir = Path(input_dir_path)
    output_file = Path(output_file_path)
    
    if not input_dir.is_dir():
        print(f"Error: Directory '{input_dir_path}' does not exist.")
        return

    with open(output_file, mode="w", encoding="utf-8") as out:
        # Find all .csv files (case-insensitive)
        csv_files = sorted(list(input_dir.glob("*.csv")) + list(input_dir.glob("*.CSV")))
        
        if not csv_files:
            print(f"No CSV files found in '{input_dir_path}'.")
            return
            
        for file_path in csv_files:
            # Skip the output file if it's placed in the same directory
            if file_path.resolve() == output_file.resolve():
                continue
                
            out.write(f"{'='*60}\n")
            out.write(f" FILE: {file_path.name}\n")
            out.write(f"{'='*60}\n\n")
            
            try:
                with open(file_path, mode="r", newline="", encoding="utf-8-sig") as f:
                    reader = csv.reader(f)
                    rows = list(reader)
                    
                    if not rows:
                        out.write("[Empty File]\n\n")
                        continue
                    
                    # Calculate maximum width for each column to handle alignment
                    col_widths = []
                    for col_idx in range(max(len(row) for row in rows)):
                        max_len = 0
                        for row in rows:
                            if col_idx < len(row):
                                max_len = max(max_len, len(str(row[col_idx])))
                        col_widths.append(max_len)
                    
                    # Write rows with clean column spacing
                    for row in rows:
                        formatted_row = []
                        for idx, cell in enumerate(row):
                            # Left-align text based on calculated max width plus padding
                            formatted_row.append(f"{cell:<{col_widths[idx]}}")
                        
                        # Join columns using a tab or arbitrary spacer
                        out.write("   ".join(formatted_row) + "\n")
                        
                out.write("\n\n") # Spacing before the next file section
                print(f"Processed: {file_path.name}")
                
            except Exception as e:
                out.write(f"[ERROR PROCESSING FILE: {str(e)}]\n\n")
                print(f"Error reading {file_path.name}: {e}")

        print(f"\nSuccessfully created combined text file: {output_file.resolve()}")

if __name__ == "__main__":
    # Change these paths to match your system setup
    INPUT_DIRECTORY = "./out"
    OUTPUT_TEXT_FILE = "./combined_output.txt"
    
    convert_csv_dir_to_txt(INPUT_DIRECTORY, OUTPUT_TEXT_FILE)
