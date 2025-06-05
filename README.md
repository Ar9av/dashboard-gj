# PVTG Survey Dashboard 📊

A comprehensive interactive dashboard for analyzing Particularly Vulnerable Tribal Groups (PVTG) survey data from Gujarat. This dashboard provides powerful filtering, visualization, and data analysis capabilities for the survey data in Gujarati.

## Features

### 🔍 **Advanced Filtering**
- **Geographic Filters**: Filter by District (જિલ્લો), Taluka (તાલુકો), and Village (ગામનું નામ)
- **Smart Search**: Search across all columns with real-time filtering
- **Cascading Filters**: Filters update dynamically based on selections

### 📊 **Interactive Visualizations**
- **Overview Tab**: District and Taluka distribution charts
- **Geographic Analysis**: Population vs Households scatter plots
- **Detailed Analytics**: Housing types and water source analysis
- **Real-time Metrics**: Total records, villages, households, and population

### 📋 **Data Management**
- **Customizable Data Table**: Select which columns to display
- **Export Functionality**: Download filtered data as CSV
- **Responsive Design**: Works on desktop and mobile devices

### 🎨 **Modern UI/UX**
- Clean, professional interface with Gujarati language support
- Gradient metric cards with key statistics
- Tabbed navigation for organized content
- Beautiful visualizations with Plotly

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Dashboard
```bash
streamlit run dashboard.py
```

### 3. Access the Dashboard
Open your web browser and navigate to `http://localhost:8501`

## Data Structure

The dashboard automatically processes your XLSX file with 51 columns including:

### Key Data Fields
- **ક્રમ**: Serial number
- **ગામનું નામ**: Village name
- **ફળિયાનું નામ**: Hamlet name
- **ગ્રામ પંચાયતનું નામ**: Gram Panchayat name
- **તાલુકો**: Taluka
- **જિલ્લો**: District
- **ગામના કુલ ઘરોની સંખ્યા**: Total households in village
- **ગામની કુલ વસ્તી**: Total village population
- **કુલ ઘરો પૈકી આદિમજુથના ઘરોની સંખ્યા**: Tribal households
- **કુલ વસ્તી પૈકી આદિમજુથની વસ્તી**: Tribal population

### Infrastructure & Services
- **આવાસની વિગત**: Housing details
- **પીવાના પાણીનો સ્ત્રોત**: Water source
- **વીજળીની સુવિધા**: Electricity facility
- **શૌચાલયની સુવિધા**: Toilet facility
- **આરોગ્યની સુવિધા**: Health facility
- **શિક્ષણની સુવિધા**: Education facility

### Government Schemes
- **રેશનકાર્ડની વિગત**: Ration card details
- **મનરેગા જોબકાર્ડની વિગત**: MGNREGA job card
- **આધારકાર્ડ**: Aadhaar card
- **PM JAY કાર્ડ**: PM-JAY card
- **જન ધન બેંક ખાતું**: Jan Dhan bank account
- **ઉજ્જવલા યોજના**: Ujjwala scheme
- **PM KISAN સન્માન નિધિ યોજના**: PM-KISAN scheme

## Usage Guide

### Filtering Data
1. **Select Geographic Filters**: Use the sidebar to filter by district, taluka, or village
2. **Search**: Use the search box to find specific records across all columns
3. **View Metrics**: Monitor the filtered results with real-time metric cards

### Exploring Visualizations
1. **Overview Tab**: Get a high-level view of data distribution
2. **Geographic Analysis Tab**: Analyze population and household relationships
3. **Data Table Tab**: View and export filtered data
4. **Detailed Analytics Tab**: Explore housing and infrastructure data

### Exporting Data
1. Navigate to the "Data Table" tab
2. Select the columns you want to include
3. Click "Download CSV" to export filtered data

## Technical Details

### Built With
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **OpenPyXL**: Excel file processing

### Performance Features
- **Data Caching**: Efficient data loading with Streamlit caching
- **Responsive Design**: Optimized for various screen sizes
- **Fast Filtering**: Real-time filter updates without page refresh

## File Structure
```
dashboard/
├── dashboard.py          # Main dashboard application
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── analyze_data.py      # Data analysis utility
└── 7 Villages PVTGs survey - 2025.xlsx  # Your data file
```

## Troubleshooting

### Common Issues
1. **Module not found**: Run `pip install -r requirements.txt`
2. **File not found**: Ensure the XLSX file is in the same directory
3. **Performance issues**: The dashboard uses caching for optimal performance

### Browser Compatibility
- Works best in Chrome, Firefox, Safari, and Edge
- JavaScript must be enabled
- Minimum screen resolution: 1024x768

## Contributing

Feel free to enhance the dashboard by:
- Adding new visualization types
- Improving the UI/UX
- Adding export formats (PDF, Excel)
- Including more analytical features

## Support

For questions or issues:
1. Check this README file
2. Review the error messages in the terminal
3. Ensure all dependencies are properly installed

---

**Happy Analyzing! 🚀**

*This dashboard was built to help analyze PVTG survey data effectively and make data-driven decisions for tribal welfare programs.* 