import sys
sys.path.append('\Desktop\Power meter')
import main_pm

def run():
    try:
        main_pm.insert_db()
    except Exception as e:
        print(e)

def main():
    run()

if __name__ == '__main__':
    main()