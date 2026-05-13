"""
Design System & Styles for Islamic Science Kids Book
Manages colors, fonts, and typography
"""

from reportlab.lib import colors
from reportlab.lib.units import mm, pt
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ============================================================================
# COLOR PALETTE
# ============================================================================

class Colors:
    """Premium color system for the book"""
    
    # Primary Colors
    PRIMARY_PURPLE = colors.HexColor("#6B4DFF")
    PRIMARY_INDIGO = colors.HexColor("#4C3DD9")
    PRIMARY_GOLD = colors.HexColor("#FFD700")
    
    # Secondary Colors
    SAGE_GREEN = colors.HexColor("#7CB342")
    OCEAN_BLUE = colors.HexColor("#0288D1")
    CORAL_PINK = colors.HexColor("#FF7043")
    SUNSET_ORANGE = colors.HexColor("#FFA726")
    
    # Neutrals
    CREAM = colors.HexColor("#FFFBF0")
    SOFT_WHITE = colors.HexColor("#FFFFFF")
    LIGHT_GRAY = colors.HexColor("#F5F5F5")
    MEDIUM_GRAY = colors.HexColor("#BDBDBD")
    DARK_GRAY = colors.HexColor("#424242")
    
    # Accents
    ISLAMIC_GOLD = colors.HexColor("#D4AF37")
    AYAH_BOX_BG = colors.HexColor("#FFF8DC")
    STORY_BG = colors.HexColor("#F0E6FF")
    SCIENCE_BG = colors.HexColor("#E0F2F1")
    FACT_BG = colors.HexColor("#FFF3E0")


# ============================================================================
# TYPOGRAPHY SYSTEM
# ============================================================================

class Typography:
    """Font sizes and styles following child-friendly design"""
    
    # Cover & Section Headers
    COVER_TITLE = 72  # pt
    SECTION_TITLE = 48  # pt
    CHAPTER_TITLE = 42  # pt
    CHAPTER_NUMBER = 36  # pt
    
    # Main Content
    HEADING_1 = 28  # pt
    HEADING_2 = 24  # pt
    HEADING_3 = 20  # pt
    BODY_TEXT = 16  # pt
    BODY_SMALL = 14  # pt
    CAPTION = 12  # pt
    
    # Arabic Text
    ARABIC_AYAH = 24  # pt
    ARABIC_SURAH = 14  # pt
    TRANSLATION = 16  # pt


# ============================================================================
# FONTS
# ============================================================================

def register_fonts():
    """Register custom fonts - with fallbacks if unavailable"""
    
    try:
        # Try to register Fredoka for headings
        pdfmetrics.registerFont(TTFont('Fredoka', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'))
    except:
        print("⚠️  Fredoka not found, using default font")
    
    try:
        # Try to register Nunito for body text
        pdfmetrics.registerFont(TTFont('Nunito', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'))
    except:
        print("⚠️  Nunito not found, using default font")
    
    try:
        # Try to register Amiri for Arabic
        pdfmetrics.registerFont(TTFont('Amiri', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'))
    except:
        print("⚠️  Amiri not found, using default font")


class Fonts:
    """Font family definitions with graceful fallbacks"""
    
    HEADING_FONT = "Helvetica-Bold"  # Fredoka fallback
    BODY_FONT = "Helvetica"  # Nunito fallback
    ARABIC_FONT = "Helvetica"  # Amiri fallback


# ============================================================================
# SPACING SYSTEM
# ============================================================================

class Spacing:
    """Consistent spacing throughout the book"""
    
    XS = 4 * mm
    SM = 8 * mm
    MD = 12 * mm
    LG = 16 * mm
    XL = 24 * mm
    XXL = 32 * mm
    XXXL = 48 * mm
    
    # Page margins
    PAGE_MARGIN = 20 * mm
    INSIDE_MARGIN = 18 * mm
    TOP_MARGIN = 20 * mm
    BOTTOM_MARGIN = 20 * mm


# ============================================================================
# BORDER RADIUS
# ============================================================================

class BorderRadius:
    """Rounded corners for modern design"""
    
    SMALL = 4
    MEDIUM = 8
    LARGE = 12
    XLARGE = 16


# ============================================================================
# SHADOW SYSTEM
# ============================================================================

class Shadows:
    """Drop shadow effects for depth"""
    
    LIGHT = 1
    MEDIUM = 2
    STRONG = 4


# ============================================================================
# PAGE DIMENSIONS
# ============================================================================

class PageDimensions:
    """Standard page sizes"""
    
    WIDTH = 210 * mm  # A4 width
    HEIGHT = 297 * mm  # A4 height
    
    # Safe printable area
    CONTENT_WIDTH = WIDTH - (2 * Spacing.PAGE_MARGIN)
    CONTENT_HEIGHT = HEIGHT - (2 * Spacing.PAGE_MARGIN)


# ============================================================================
# GRADIENT DEFINITIONS
# ============================================================================

class Gradients:
    """Common gradient combinations"""
    
    # Cover gradient
    COVER_START = colors.HexColor("#6B4DFF")  # Purple
    COVER_END = colors.HexColor("#1A1A2E")    # Dark indigo
    
    # Chapter gradient
    CHAPTER_START = colors.HexColor("#E8D5FF")  # Light purple
    CHAPTER_END = colors.HexColor("#FFFFFF")    # White
    
    # Section gradient
    SECTION_START = colors.HexColor("#F0E6FF")  # Very light purple
    SECTION_END = colors.HexColor("#FFFFFF")    # White
