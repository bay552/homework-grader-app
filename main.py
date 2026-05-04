"""
小学作业 AI 批改应用
功能：拍照 → OCR 识别 → AI 批改 → 显示结果
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
import os
import json

# 设置窗口大小（移动端适配）
Window.size = (360, 640)


class HomeworkGraderApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_image_path = None
        self.grading_result = None
        
    def build(self):
        self.title = "作业批改 AI"
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title_label = Label(
            text='📚 小学作业 AI 批改',
            font_size='24sp',
            bold=True,
            size_hint=(1, 0.1)
        )
        main_layout.add_widget(title_label)
        
        # 图片显示区域
        self.image_widget = Image(
            source='',
            size_hint=(1, 0.4),
            allow_stretch=True,
            keep_ratio=True
        )
        main_layout.add_widget(self.image_widget)
        
        # 拍照按钮
        self.camera_btn = Button(
            text='📸 拍照/上传作业',
            font_size='18sp',
            size_hint=(1, 0.1)
        )
        self.camera_btn.bind(on_press=self.open_camera)
        main_layout.add_widget(self.camera_btn)
        
        # 批改按钮
        self.grade_btn = Button(
            text='🤖 AI 智能批改',
            font_size='18sp',
            size_hint=(1, 0.1),
            disabled=True
        )
        self.grade_btn.bind(on_press=self.grade_homework)
        main_layout.add_widget(self.grade_btn)
        
        # 结果显示
        self.result_label = Label(
            text='请先上传作业照片',
            font_size='16sp',
            size_hint=(1, 0.2),
            halign='center',
            valign='middle'
        )
        self.result_label.bind(
            size=self.instance_label,
            texture_size=self.instance_label
        )
        main_layout.add_widget(self.result_label)
        
        return main_layout
    
    def open_camera(self, instance):
        """打开相机或文件选择器"""
        # 简化版本：使用文件选择器
        # 实际 Android 版本会使用 plyer.camera
        try:
            from plyer import filechooser
            filechooser.choose_file(
                on_select=self.on_file_selected,
                filters=[('Images', '*.png', '*.jpg', '*.jpeg')]
            )
        except ImportError:
            # 桌面测试模式
            self.result_label.text = "📱 在手机上使用时会打开相机"
            self.current_image_path = "test_image"
            self.image_widget.source = "https://via.placeholder.com/300x400?text=作业照片"
            self.grade_btn.disabled = False
    
    def on_file_selected(self, selection):
        """处理选中的文件"""
        if selection:
            self.current_image_path = selection[0]
            self.image_widget.source = self.current_image_path
            self.grade_btn.disabled = False
    
    def grade_homework(self, instance):
        """AI 批改作业"""
        if not self.current_image_path:
            return
        
        self.result_label.text = "🔄 正在批改中..."
        self.grade_btn.disabled = True
        
        # 模拟 AI 批改过程
        Clock.schedule_once(self.show_grading_result, 2)
    
    def show_grading_result(self, dt):
        """显示批改结果"""
        # 示例批改结果（实际应调用 AI API）
        self.grading_result = {
            'score': 95,
            'correct': 19,
            'wrong': 1,
            'feedback': '做得很好！注意单位换算哦~'
        }
        
        result_text = (
            f"✅ 批改完成!\n\n"
            f"得分：{self.grading_result['score']}分\n"
            f"正确：{self.grading_result['correct']}题\n"
            f"错误：{self.grading_result['wrong']}题\n\n"
            f"💡 {self.grading_result['feedback']}"
        )
        
        self.result_label.text = result_text
        self.grade_btn.disabled = False


if __name__ == '__main__':
    HomeworkGraderApp().run()
