import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import hashlib

# Set page configuration
st.set_page_config(
    page_title="PVTG Survey Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Authentication configuration
USERS = {
    "admin": "admin123",
    "analyst": "analyst456",
    "viewer": "viewer789"
}

def hash_password(password):
    """Hash password for basic security"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(username, password):
    """Verify username and password"""
    if username in USERS:
        return USERS[username] == password
    return False

def login_form():
    """Display login form"""
    st.markdown("""
    <style>
        .login-container {
            max-width: 400px;
            margin: 0 auto;
            padding: 2rem;
            background: #f8f9fa;
            border-radius: 10px;
            border: 2px solid #e9ecef;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-top: 5rem;
        }
        .login-header {
            text-align: center;
            color: #0066cc;
            margin-bottom: 2rem;
        }
        .login-info {
            background: #e3f2fd;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            border-left: 4px solid #2196f3;
        }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<h2 class="login-header" style="color: black;">🔐 PVTG Dashboard Login</h2>', unsafe_allow_html=True)
        
            #         <strong>Demo Credentials:</strong><br>
            # • Username: <code>admin</code> Password: <code>admin123</code><br>
            # • Username: <code>analyst</code> Password: <code>analyst456</code><br>
            # • Username: <code>viewer</code> Password: <code>viewer789</code>
        # Demo credentials info
        st.markdown("""
        <div class="login-info">
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("👤 Username")
            password = st.text_input("🔑 Password", type="password")
            submit_button = st.form_submit_button("🚀 Login", use_container_width=True)
            
            if submit_button:
                if verify_password(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
        
        st.markdown('</div>', unsafe_allow_html=True)

def logout_sidebar():
    """Add logout option to sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"👤 **Logged in as:** {st.session_state.username}")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()

# Custom CSS for light theme styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0066cc;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa;
        border: 2px solid #e9ecef;
        padding: 1.5rem;
        border-radius: 10px;
        color: #495057;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metric-card h3 {
        color: #0066cc;
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
    }
    .metric-card p {
        color: #6c757d;
        margin: 0.5rem 0 0 0;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .filter-header {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .filter-header h2 {
        color: #495057;
        margin: 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        color: #495057;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0066cc !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the data"""
    df = pd.read_excel('7 Villages PVTGs survey - 2025.xlsx')
    
    # Clean column names and remove empty unnamed columns
    df.columns = [col if not col.startswith('Unnamed') else f'કૉલમ {col.split(":")[1].strip()}' 
                  for col in df.columns]
    
    # Remove the header row that contains column numbers
    df = df.iloc[2:].reset_index(drop=True)
    
    # Convert numeric columns
    numeric_cols = ['ક્રમ', 'ગામના કુલ ઘરોની સંખ્યા', 'ગામની કુલ વસ્તી', 
                   'કુલ ઘરો પૈકી આદિમજુથના ઘરોની સંખ્યા', 'કુલ વસ્તી પૈકી આદિમજુથની વસ્તી',
                   'કુટુંબના સભ્યની સંખ્યા']
    
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

def main_dashboard():
    """Main dashboard content"""
    st.markdown('<h1 class="main-header">🏘️ PVTG Survey Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #6c757d;">Particularly Vulnerable Tribal Groups Survey Analysis</p>', unsafe_allow_html=True)
    
    # Load data
    with st.spinner('Loading data...'):
        df = load_data()
    
    # Sidebar filters
    st.sidebar.markdown('<div class="filter-header"><h2>🔍 Filters</h2></div>', unsafe_allow_html=True)
    
    # District filter
    districts = df['જિલ્લો'].dropna().unique()
    selected_district = st.sidebar.selectbox('જિલ્લો (District)', ['All'] + list(districts))
    
    # Taluka filter
    if selected_district != 'All':
        talukas = df[df['જિલ્લો'] == selected_district]['તાલુકો'].dropna().unique()
    else:
        talukas = df['તાલુકો'].dropna().unique()
    selected_taluka = st.sidebar.selectbox('તાલુકો (Taluka)', ['All'] + list(talukas))
    
    # Village filter
    filtered_df = df.copy()
    if selected_district != 'All':
        filtered_df = filtered_df[filtered_df['જિલ્લો'] == selected_district]
    if selected_taluka != 'All':
        filtered_df = filtered_df[filtered_df['તાલુકો'] == selected_taluka]
    
    villages = filtered_df['ગામનું નામ'].dropna().unique()
    selected_village = st.sidebar.selectbox('ગામનું નામ (Village)', ['All'] + list(villages))
    
    if selected_village != 'All':
        filtered_df = filtered_df[filtered_df['ગામનું નામ'] == selected_village]
    
    # Search functionality
    st.sidebar.markdown("---")
    search_term = st.sidebar.text_input("🔍 Search in all columns", "")
    if search_term:
        mask = filtered_df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]
    
    # Add logout to sidebar
    logout_sidebar()
    
    # Main dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'''
        <div class="metric-card">
            <h3>{len(filtered_df)}</h3>
            <p>Total Records</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        total_villages = filtered_df['ગામનું નામ'].nunique()
        st.markdown(f'''
        <div class="metric-card">
            <h3>{total_villages}</h3>
            <p>Unique Villages</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        total_households = filtered_df['ગામના કુલ ઘરોની સંખ્યા'].sum()
        if pd.isna(total_households):
            total_households = 0
        st.markdown(f'''
        <div class="metric-card">
            <h3>{int(total_households):,}</h3>
            <p>Total Households</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        total_population = filtered_df['ગામની કુલ વસ્તી'].sum()
        if pd.isna(total_population):
            total_population = 0
        st.markdown(f'''
        <div class="metric-card">
            <h3>{int(total_population):,}</h3>
            <p>Total Population</p>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visualization tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🏘️ Geographic Analysis", "📋 Data Table", "📈 Detailed Analytics"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # District wise distribution
            district_counts = filtered_df['જિલ્લો'].value_counts()
            if not district_counts.empty:
                fig = px.pie(values=district_counts.values, names=district_counts.index, 
                           title="Distribution by District",
                           color_discrete_sequence=px.colors.qualitative.Set3)
                fig.update_traces(textposition='inside', textinfo='percent+label')
                fig.update_layout(plot_bgcolor='white', paper_bgcolor='white')
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Taluka wise distribution
            taluka_counts = filtered_df['તાલુકો'].value_counts().head(10)
            if not taluka_counts.empty:
                fig = px.bar(x=taluka_counts.index, y=taluka_counts.values,
                           title="Top 10 Talukas by Record Count",
                           color_discrete_sequence=['#0066cc'])
                fig.update_layout(xaxis_title="Taluka", yaxis_title="Count",
                                plot_bgcolor='white', paper_bgcolor='white')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Geographic Distribution")
        
        # Village wise household data
        village_data = filtered_df.groupby(['ગામનું નામ', 'તાલુકો', 'જિલ્લો']).agg({
            'ગામના કુલ ઘરોની સંખ્યા': 'first',
            'ગામની કુલ વસ્તી': 'first',
            'કુલ ઘરો પૈકી આદિમજુથના ઘરોની સંખ્યા': 'first'
        }).reset_index()
        
        village_data = village_data.dropna()
        
        if not village_data.empty:
            fig = px.scatter(village_data, 
                           x='ગામના કુલ ઘરોની સંખ્યા', 
                           y='ગામની કુલ વસ્તી',
                           color='જિલ્લો',
                           hover_data=['ગામનું નામ', 'તાલુકો'],
                           title="Village Population vs Households",
                           color_discrete_sequence=px.colors.qualitative.Set2)
            fig.update_layout(plot_bgcolor='white', paper_bgcolor='white')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("Data Table")
        
        # Column selection
        all_columns = list(filtered_df.columns)
        default_columns = ['ગામનું નામ', 'તાલુકો', 'જિલ્લો', 'ગામના કુલ ઘરોની સંખ્યા', 'ગામની કુલ વસ્તી']
        selected_columns = st.multiselect(
            "Select columns to display:",
            all_columns,
            default=[col for col in default_columns if col in all_columns]
        )
        
        if selected_columns:
            display_df = filtered_df[selected_columns]
            st.dataframe(display_df, use_container_width=True)
            
            # Download button
            csv = display_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"pvtg_survey_filtered_{len(display_df)}_records.csv",
                mime="text/csv"
            )
    
    with tab4:
        st.subheader("Detailed Analytics")
        
        # Housing type analysis
        housing_col = 'આવાસની વિગત\nઘરનો પ્રકાર'
        if housing_col in filtered_df.columns:
            housing_data = filtered_df[housing_col].value_counts().head(10)
            if not housing_data.empty:
                fig = px.bar(x=housing_data.values, y=housing_data.index, 
                           orientation='h', title="Housing Types",
                           color_discrete_sequence=['#28a745'])
                fig.update_layout(plot_bgcolor='white', paper_bgcolor='white')
                st.plotly_chart(fig, use_container_width=True)
        
        # Water source analysis
        water_col = 'પીવાના પાણીનોપ સ્ત્રોત\n'
        if water_col in filtered_df.columns:
            water_data = filtered_df[water_col].value_counts().head(10)
            if not water_data.empty:
                fig = px.pie(values=water_data.values, names=water_data.index,
                           title="Water Sources",
                           color_discrete_sequence=px.colors.qualitative.Pastel)
                fig.update_layout(plot_bgcolor='white', paper_bgcolor='white')
                st.plotly_chart(fig, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 2rem;">
        <p>PVTG Survey Dashboard | Built with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application logic with authentication"""
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    
    # Show login or dashboard based on authentication status
    if not st.session_state.authenticated:
        login_form()
    else:
        main_dashboard()

if __name__ == "__main__":
    main() 