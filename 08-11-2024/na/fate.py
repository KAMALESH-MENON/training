from logic import Logic
from presentation import Presentation
from task import Task

def fate():
    print(f"Hello")
    l1 = Logic()
    p1 = Presentation()
    t1 = Task()

    p1.f1()
    l1.f2()
    t1.f3()
    
if __name__ == "__main__":
    fate()