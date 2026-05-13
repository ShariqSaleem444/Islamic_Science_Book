"""
Reusable Components for Islamic Science Kids Book
Modular UI elements for consistent design
"""

from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from styles import Colors, Typography, Spacing, Fonts, BorderRadius
import math


class Components:
    """Reusable layout components"""
    
    @staticmethod
    def create_ayah_box(arabic_text, english_text, surah_name):
        """
        Creates a beautiful Quranic verse box
        
        Args:
            arabic_text: Arabic ayah
            english_text: English translation
            surah_name: Name and number of surah
        """
        styles = getSampleStyleSheet()
        
        # Custom style for arabic
        arabic_style = ParagraphStyle(
            'ArabicAyah',
            parent=styles['Normal'],
            fontName=Fonts.ARABIC_FONT,
            fontSize=Typography.ARABIC_AYAH,
            textColor=Colors.PRIMARY_PURPLE,
            alignment=1,  # Center
            spaceAfter=8,
        )
        
        # Custom style for english
        english_style = ParagraphStyle(
            'EnglishAyah',
            parent=styles['Normal'],
            fontName=Fonts.HEADING_FONT,
            fontSize=Typography.TRANSLATION,
            textColor=Colors.DARK_GRAY,
            alignment=1,  # Center
            spaceAfter=12,
        )
        
        # Custom style for surah
        surah_style = ParagraphStyle(
            'SurahName',
            parent=styles['Normal'],
            fontName=Fonts.BODY_FONT,
            fontSize=Typography.CAPTION,
            textColor=Colors.ISLAMIC_GOLD,
            alignment=1,  # Center
        )
        
        return [
            Spacer(1, Spacing.MD),
            Paragraph(f"✨ {arabic_text} ✨", arabic_style),
            Spacer(1, Spacing.SM),
            Paragraph(f'"{english_text}"', english_style),
            Spacer(1, Spacing.XS),
            Paragraph(surah_name, surah_style),
            Spacer(1, Spacing.MD),
        ]
    
    @staticmethod
    def create_story_card(title, content):
        """
        Creates a story narrative card
        
        Args:
            title: Story section title
            content: Story text
        """
        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle(
            'StoryTitle',
            parent=styles['Heading2'],
            fontName=Fonts.HEADING_FONT,
            fontSize=Typography.HEADING_2,
            textColor=Colors.PRIMARY_PURPLE,
            spaceAfter=12,
        )
        
        body_style = ParagraphStyle(
            'StoryBody',
            parent=styles['Normal'],
            fontName=Fonts.BODY_FONT,
            fontSize=Typography.BODY_TEXT,
            textColor=Colors.DARK_GRAY,
            leading=22,
            spaceAfter=12,
            alignment=4,  # Justified
        )
        
        return [
            Spacer(1, Spacing.SM),
            Paragraph(f"📖 {title}", title_style),
            Spacer(1, Spacing.SM),
            Paragraph(content, body_style),
            Spacer(1, Spacing.MD),
        ]
    
    @staticmethod
    def create_science_box(title, content):
        """
        Creates a science explanation box
        
        Args:
            title: Science concept title
            content: Explanation text with bullet points
        """
        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle(
            'ScienceTitle',
            parent=styles['Heading2'],
            fontName=Fonts.HEADING_FONT,
            fontSize=Typography.HEADING_2,
            textColor=Colors.OCEAN_BLUE,
            spaceAfter=12,
        )
        
        body_style = ParagraphStyle(
            'ScienceBody',
            parent=styles['Normal'],
            fontName=Fonts.BODY_FONT,
            fontSize=Typography.BODY_TEXT,
            textColor=Colors.DARK_GRAY,
            leading=20,
            spaceAfter=8,
        )
        
        return [
            Spacer(1, Spacing.SM),
            Paragraph(f"🔬 The Science Behind This", title_style),
            Spacer(1, Spacing.XS),
            Paragraph(content, body_style),
            Spacer(1, Spacing.MD),
        ]
    
    @staticmethod
    def create_fun_fact_card(fact_text, emoji="⭐"):
        """
        Creates a colorful fun fact card
        
        Args:
            fact_text: The fun fact
            emoji: Decorative emoji
        """
        styles = getSampleStyleSheet()
        
        fact_style = ParagraphStyle(
            'FunFact',
            parent=styles['Normal'],
            fontName=Fonts.BODY_FONT,
            fontSize=Typography.BODY_SMALL,
            textColor=Colors.DARK_GRAY,
            leading=18,
            alignment=0,
        )
        
        return Paragraph(f"{emoji} {fact_text}", fact_style)
    
    @staticmethod
    def create_quiz_question(question_text):
        """
        Creates an interactive quiz question
        
        Args:
            question_text: The question to ask
        """
        styles = getSampleStyleSheet()
        
        quiz_style = ParagraphStyle(
            'QuizQuestion',
            parent=styles['Normal'],
            fontName=Fonts.BODY_FONT,
            fontSize=Typography.BODY_TEXT,
            textColor=Colors.PRIMARY_PURPLE,
            leading=20,
            spaceAfter=12,
        )
        
        return [
            Spacer(1, Spacing.SM),
            Paragraph(f"💭 <b>Think About It:</b> {question_text}", quiz_style),
            Spacer(1, Spacing.SM),
        ]
    
    @staticmethod
    def create_lesson_box(lessons_list):
        """
        Creates a lesson summary box
        
        Args:
            lessons_list: List of 3 key lessons learned
        """
        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle(
            'LessonTitle',
            parent=styles['Heading2'],
            fontName=Fonts.HEADING_FONT,
            fontSize=Typography.HEADING_2,
            textColor=Colors.SAGE_GREEN,
            spaceAfter=12,
        )
        
        lesson_style = ParagraphStyle(
            'LessonItem',
            parent=styles['Normal'],
            fontName=Fonts.BODY_FONT,
            fontSize=Typography.BODY_TEXT,
            textColor=Colors.DARK_GRAY,
            leading=18,
            leftIndent=20,
            spaceAfter=8,
        )
        
        elements = [
            Spacer(1, Spacing.SM),
            Paragraph("✨ What We Learned", title_style),
            Spacer(1, Spacing.XS),
        ]
        
        for i, lesson in enumerate(lessons_list, 1):
            elements.append(Paragraph(f"<b>{i}.</b> {lesson}", lesson_style))
        
        elements.append(Spacer(1, Spacing.MD))
        return elements
    
    @staticmethod
    def create_chapter_badge(chapter_number, chapter_title):
        """
        Creates a chapter number badge
        
        Args:
            chapter_number: Chapter number
            chapter_title: Chapter title
        """
        styles = getSampleStyleSheet()
        
        badge_style = ParagraphStyle(
            'ChapterBadge',
            parent=styles['Normal'],
            fontName=Fonts.HEADING_FONT,
            fontSize=Typography.CHAPTER_NUMBER,
            textColor=Colors.PRIMARY_PURPLE,
            alignment=1,
        )
        
        title_style = ParagraphStyle(
            'ChapterTitleText',
            parent=styles['Heading1'],
            fontName=Fonts.HEADING_FONT,
            fontSize=Typography.CHAPTER_TITLE,
            textColor=Colors.PRIMARY_INDIGO,
            alignment=1,
            spaceAfter=12,
        )
        
        return [
            Spacer(1, Spacing.XXXL),
            Paragraph(f"Chapter {chapter_number}", badge_style),
            Spacer(1, Spacing.MD),
            Paragraph(chapter_title, title_style),
            Spacer(1, Spacing.XXXL),
        ]
    
    @staticmethod
    def create_reflection_prompt(reflection_text):
        """
        Creates a reflection prompt for deeper thinking
        
        Args:
            reflection_text: The reflection question or prompt
        """
        styles = getSampleStyleSheet()
        
        reflection_style = ParagraphStyle(
            'ReflectionPrompt',
            parent=styles['Normal'],
            fontName=Fonts.BODY_FONT,
            fontSize=Typography.BODY_TEXT,
            textColor=Colors.CORAL_PINK,
            leading=18,
            spaceAfter=12,
            italic=True,
        )
        
        return [
            Spacer(1, Spacing.SM),
            Paragraph(f"🤔 <b>Reflection:</b> {reflection_text}", reflection_style),
            Spacer(1, Spacing.MD),
        ]
    
    @staticmethod
    def create_achievement_badge(achievement_text):
        """
        Creates an achievement badge
        
        Args:
            achievement_text: The achievement or accomplishment
        """
        styles = getSampleStyleSheet()
        
        badge_style = ParagraphStyle(
            'AchievementBadge',
            parent=styles['Normal'],
            fontName=Fonts.HEADING_FONT,
            fontSize=Typography.BODY_TEXT,
            textColor=Colors.SOFT_WHITE,
            alignment=1,
            spaceAfter=8,
        )
        
        return [
            Spacer(1, Spacing.SM),
            Paragraph(f"🏆 <b>{achievement_text}</b>", badge_style),
            Spacer(1, Spacing.SM),
        ]


def create_page_break():
    """Creates a page break"""
    return PageBreak()


def create_spacer(size="md"):
    """
    Creates a spacer with standardized sizes
    
    Args:
        size: 'xs', 'sm', 'md', 'lg', 'xl', 'xxl', 'xxxl'
    """
    size_map = {
        'xs': Spacing.XS,
        'sm': Spacing.SM,
        'md': Spacing.MD,
        'lg': Spacing.LG,
        'xl': Spacing.XL,
        'xxl': Spacing.XXL,
        'xxxl': Spacing.XXXL,
    }
    return Spacer(1, size_map.get(size, Spacing.MD))
