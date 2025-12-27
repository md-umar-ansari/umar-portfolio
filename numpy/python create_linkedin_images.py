import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import io

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
colors = {
    'primary': '#2E7D32',      # Green
    'secondary': '#1976D2',    # Blue
    'accent': '#F57C00',       # Orange
    'background': '#F5F5F5',
    'text': '#212121'
}

# ============================================
# IMAGE 1: TITLE SLIDE
# ============================================
def create_slide_1():
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
    
    # Background gradient
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack((gradient, gradient))
    
    ax.imshow([[0, 1], [0, 1]], extent=[0, 10, 0, 10], 
              cmap='RdYlGn', aspect='auto', alpha=0.8)
    
    # Title
    ax.text(5, 7, '🚀 SAMARTH', 
            fontsize=80, weight='bold', ha='center', va='center',
            color='#2E7D32', family='sans-serif')
    
    ax.text(5, 5.5, 'Data Visualization App', 
            fontsize=50, ha='center', va='center',
            color='#1976D2', family='sans-serif', weight='bold')
    
    ax.text(5, 4, 'Building Smart Agricultural Insights with Python', 
            fontsize=32, ha='center', va='center',
            color='#212121', family='sans-serif', style='italic')
    
    # Bottom accent
    ax.add_patch(patches.Rectangle((1, 0.5), 8, 0.3, 
                                    facecolor='#F57C00', edgecolor='none'))
    
    ax.text(5, 1.5, '📊 Data Engineering | 🌾 Agriculture | 💡 Innovation', 
            fontsize=24, ha='center', va='center', color='#212121')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide_1_title.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Slide 1 Created: slide_1_title.png")

# ============================================
# IMAGE 2: PROJECT OVERVIEW
# ============================================
def create_slide_2():
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
    ax.set_facecolor('#F5F5F5')
    
    # Title
    ax.text(0.5, 0.95, 'SAMARTH APP - Project Highlights', 
            fontsize=48, weight='bold', ha='center', va='top',
            transform=ax.transAxes, color='#2E7D32', family='sans-serif')
    
    # Features
    features = [
        '✓ Real-time crop & rainfall data analysis',
        '✓ Multi-district, multi-year dataset processing',
        '✓ Actionable agricultural insights visualization',
        '✓ Pandas-powered data engineering'
    ]
    
    y_pos = 0.80
    for i, feature in enumerate(features):
        # Feature box
        ax.add_patch(patches.FancyBboxPatch((0.1, y_pos - 0.08), 0.8, 0.10,
                                             boxstyle="round,pad=0.01",
                                             transform=ax.transAxes,
                                             facecolor='#E8F5E9', 
                                             edgecolor='#2E7D32', linewidth=2))
        
        ax.text(0.15, y_pos - 0.03, feature, 
                fontsize=28, ha='left', va='center',
                transform=ax.transAxes, color='#212121', weight='bold')
        
        y_pos -= 0.15
    
    # Tech Stack
    ax.text(0.5, 0.15, 'Tech Stack', 
            fontsize=36, weight='bold', ha='center', va='center',
            transform=ax.transAxes, color='#1976D2')
    
    ax.text(0.5, 0.05, 'Python | Pandas | Matplotlib | CSV Data Processing', 
            fontsize=28, ha='center', va='center',
            transform=ax.transAxes, color='#F57C00', weight='bold', 
            family='monospace')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide_2_overview.png', dpi=300, bbox_inches='tight', 
                facecolor='#F5F5F5', edgecolor='none')
    plt.close()
    print("✅ Slide 2 Created: slide_2_overview.png")

# ============================================
# IMAGE 3: CODE SNIPPET
# ============================================
def create_slide_3():
    fig, ax = plt.subplots(figsize=(10, 12), dpi=300)
    ax.set_facecolor('#1E1E1E')
    
    # Title
    ax.text(0.5, 0.97, 'Core Code Implementation', 
            fontsize=40, weight='bold', ha='center', va='top',
            transform=ax.transAxes, color='#4EC9B0', family='monospace')
    
    code_text = """# SAMARTH APP - Key Code Snippet
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
crops_df = pd.read_csv('crop_data.csv')
rainfall_df = pd.read_csv('rainfall_data.csv')

# Merge by district and year
merged = pd.merge(crops_df, rainfall_df,
                  on=['District', 'Year'])

# Analyze production trends
production = merged.groupby(
    'District')['Production'].sum()

# Visualize insights
production.plot(kind='bar', color='green')
plt.title('District-wise Production')
plt.show()"""
    
    ax.text(0.05, 0.90, code_text, 
            fontsize=14, ha='left', va='top',
            transform=ax.transAxes, color='#D4D4D4', family='monospace',
            bbox=dict(boxstyle='round', facecolor='#2D2D2D', 
                     edgecolor='#4EC9B0', linewidth=2, pad=1))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide_3_code.png', dpi=300, bbox_inches='tight', 
                facecolor='#1E1E1E', edgecolor='none')
    plt.close()
    print("✅ Slide 3 Created: slide_3_code.png")

# ============================================
# IMAGE 4: DATA VISUALIZATION
# ============================================
def create_slide_4():
    fig = plt.figure(figsize=(10, 12), dpi=300)
    fig.patch.set_facecolor('#F5F5F5')
    
    # Create grid for subplots
    gs = fig.add_gridspec(3, 1, hspace=0.4)
    
    # Title
    ax_title = fig.add_subplot(gs[0])
    ax_title.text(0.5, 0.8, 'Data Output & Visualizations', 
                  fontsize=40, weight='bold', ha='center', va='center',
                  transform=ax_title.transAxes, color='#2E7D32')
    ax_title.axis('off')
    
    # Chart 1: Bar Chart
    ax1 = fig.add_subplot(gs[1])
    districts = ['Nashik', 'Pune', 'Ahmednagar', 'Solapur', 'Sangli']
    production = [2450, 2180, 1920, 1650, 1540]
    
    bars = ax1.bar(districts, production, color='#2E7D32', edgecolor='#1B5E20', linewidth=2)
    ax1.set_ylabel('Production (1000 Tonnes)', fontsize=14, weight='bold')
    ax1.set_title('District-wise Crop Production', fontsize=16, weight='bold', color='#1976D2')
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_facecolor('#FFFFFF')
    
    for i, (bar, val) in enumerate(zip(bars, production)):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, 
                f'{val}K', ha='center', va='bottom', fontsize=11, weight='bold')
    
    # Chart 2: Scatter Plot
    ax2 = fig.add_subplot(gs[2])
    rainfall = np.random.normal(600, 100, 50)
    prod = rainfall * 3.5 + np.random.normal(0, 200, 50)
    
    ax2.scatter(rainfall, prod, s=150, alpha=0.6, c='#1976D2', edgecolors='#0D47A1', linewidth=1.5)
    ax2.set_xlabel('Rainfall (mm)', fontsize=14, weight='bold')
    ax2.set_ylabel('Production (Tonnes)', fontsize=14, weight='bold')
    ax2.set_title('Rainfall vs Production Correlation', fontsize=16, weight='bold', color='#1976D2')
    ax2.grid(True, alpha=0.3)
    ax2.set_facecolor('#FFFFFF')
    
    plt.savefig('slide_4_data.png', dpi=300, bbox_inches='tight', 
                facecolor='#F5F5F5', edgecolor='none')
    plt.close()
    print("✅ Slide 4 Created: slide_4_data.png")

# ============================================
# IMAGE 5: CALL-TO-ACTION & SKILLS
# ============================================
def create_slide_5():
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
    ax.set_facecolor('#F5F5F5')
    
    # Title
    ax.text(0.5, 0.95, 'Skills & Opportunities', 
            fontsize=48, weight='bold', ha='center', va='top',
            transform=ax.transAxes, color='#2E7D32')
    
    # Key Skills
    ax.text(0.5, 0.85, 'KEY SKILLS DEMONSTRATED', 
            fontsize=32, weight='bold', ha='center', va='top',
            transform=ax.transAxes, color='#1976D2')
    
    skills = [
        '✓ Data Engineering & Processing (Pandas)',
        '✓ Statistical Analysis & Correlation',
        '✓ Data Visualization (Matplotlib)',
        '✓ Python Programming & Debugging',
        '✓ Real-world Problem Solving'
    ]
    
    y_pos = 0.78
    for skill in skills:
        ax.text(0.1, y_pos, skill, 
                fontsize=20, ha='left', va='center',
                transform=ax.transAxes, color='#212121', weight='bold')
        y_pos -= 0.10
    
    # Looking For Section
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.15), 0.9, 0.35,
                                         boxstyle="round,pad=0.02",
                                         transform=ax.transAxes,
                                         facecolor='#E3F2FD', 
                                         edgecolor='#1976D2', linewidth=3))
    
    ax.text(0.5, 0.45, 'LOOKING FOR OPPORTUNITIES IN:', 
            fontsize=28, weight='bold', ha='center', va='top',
            transform=ax.transAxes, color='#1976D2')
    
    opportunities = [
        '→ Data Science & Analytics',
        '→ Agricultural Technology (AgriTech)',
        '→ Business Intelligence'
    ]
    
    y_pos = 0.38
    for opp in opportunities:
        ax.text(0.5, y_pos, opp, 
                fontsize=22, ha='center', va='center',
                transform=ax.transAxes, color='#2E7D32', weight='bold')
        y_pos -= 0.08
    
    # CTA
    ax.text(0.5, 0.08, "Let's Connect! 🤝 Open to Opportunities", 
            fontsize=26, ha='center', va='center',
            transform=ax.transAxes, color='#F57C00', weight='bold',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFF3E0', 
                     edgecolor='#F57C00', linewidth=2))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('slide_5_cta.png', dpi=300, bbox_inches='tight', 
                facecolor='#F5F5F5', edgecolor='none')
    plt.close()
    print("✅ Slide 5 Created: slide_5_cta.png")

# ============================================
# GENERATE ALL IMAGES
# ============================================
if __name__ == "__main__":
    print("\n🎨 Generating LinkedIn Carousel Images...\n")
    
    create_slide_1()
    create_slide_2()
    create_slide_3()
    create_slide_4()
    create_slide_5()
    
    print("\n✅ All 5 images created successfully!")
    print("\n📁 Files generated:")
    print("   • slide_1_title.png")
    print("   • slide_2_overview.png")
    print("   • slide_3_code.png")
    print("   • slide_4_data.png")
    print("   • slide_5_cta.png")
    print("\n🚀 Ready to upload to LinkedIn!")
