from datetime import datetime

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')

if __name__ == "__main__":
    print("The latest date is:", get_current_date())