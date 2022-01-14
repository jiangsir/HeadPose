import classes.ClassOpenCV
import fire
class HeadPose:
    # def __init__(self) -> None:
    #     classes.ClassOpenCV.show_opencv('請按 ESC 離開')


    def show(self):
        '''
        顯示主畫面
        '''
        classes.ClassOpenCV.show_opencv('請按 ESC 離開')

    def always(self):
        '''
        不能使用 esc 跳出。
        '''
        classes.ClassOpenCV.show_opencv(allowESC=False)

if __name__ == '__main__':
    fire.Fire(HeadPose)