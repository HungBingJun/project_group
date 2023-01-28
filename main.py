from pathlib import Path
import cash_on_hand, overheads, profit_loss
home = Path.cwd()
file_path = home/"summary_report.txt"
file_path.touch()

summary = [overheads.overheads(),
           "\n",cash_on_hand.cash_on_hand(),
           "\n",profit_loss.profit_loss()]
with file_path.open(mode = "w", encoding ="UTF-8") as file:
    file.writelines(summary)

