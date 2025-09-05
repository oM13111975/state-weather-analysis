# import tkinter as tk
# from tkinter import ttk, messagebox
# import requests
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import pandas as pd
# from datetime import datetime
# import heapq
# from ttkthemes import ThemedTk

# class PriorityQueue:
#     def __init__(self, is_max=False):
#         self.heap = []
#         self.is_max = is_max

#     def push(self, key, value):
#         if self.is_max:
#             key = -key
#         heapq.heappush(self.heap, (key, value))

#     def pop(self):
#         key, value = heapq.heappop(self.heap)
#         if self.is_max:
#             key = -key
#         return (key, value)

#     def size(self):
#         return len(self.heap)

#     def get_sorted_items(self):
#         temp_heap = list(self.heap)
#         sorted_items = []
#         while temp_heap:
#             key, value = heapq.heappop(temp_heap)
#             if self.is_max:
#                 key = -key
#             sorted_items.append((key, value))
#         sorted_items.sort(reverse=self.is_max)
#         return sorted_items

# class WeatherAnalysisApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Weather Analysis")
#         self.root.geometry("1400x900")
        
#         self.DEFAULT_API_KEY = '0b8a3295928677e77622cb04ee7aa299' 
        
#         self.style = ttk.Style()
#         self.style.theme_use('arc')
        
#         self.style.configure('Header.TLabel', font=('Helvetica', 18, 'bold'))
#         self.style.configure('SubHeader.TLabel', font=('Helvetica', 14))
#         self.style.configure('Data.TLabel', font=('Helvetica', 12))
#         self.style.configure('Card.TFrame', relief='solid', borderwidth=1, background='#f0f0f0')
        
#         self.central_city_data = None
#         self.state_cities_data = []
#         self.current_figure = None
        
#         self.create_main_layout()
#         self.create_widgets()
        
#     def create_main_layout(self):
#         self.input_frame = ttk.Frame(self.root, padding="20 20 20 10")
#         self.input_frame.pack(fill=tk.X)
        
#         self.content_frame = ttk.Frame(self.root, padding="20 10 20 20")
#         self.content_frame.pack(fill=tk.BOTH, expand=True)
        
#         self.left_frame = ttk.Frame(self.content_frame)
#         self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
#         self.right_frame = ttk.Frame(self.content_frame)
#         self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
#     def create_widgets(self):
#         ttk.Label(self.input_frame, text="Weather Analysis Dashboard", style='Header.TLabel').pack(pady=(0, 20))
        
#         controls_frame = ttk.LabelFrame(self.input_frame, text="Controls", padding=10)
#         controls_frame.pack(fill=tk.X)
        
#         input_frame = ttk.Frame(controls_frame)
#         input_frame.pack(fill=tk.X, pady=10)
        
#         central_frame = ttk.Frame(input_frame)
#         central_frame.pack(side=tk.LEFT, padx=(0, 20))
#         ttk.Label(central_frame, text="Central City:", style='SubHeader.TLabel').pack(side=tk.LEFT)
#         self.central_city_entry = ttk.Entry(central_frame, width=20)
#         self.central_city_entry.pack(side=tk.LEFT, padx=10)
#         ttk.Button(central_frame, text="Fetch Data", command=self.fetch_central_city_data).pack(side=tk.LEFT)
        
#         state_frame = ttk.Frame(input_frame)
#         state_frame.pack(side=tk.LEFT)
#         ttk.Label(state_frame, text="State Code:", style='SubHeader.TLabel').pack(side=tk.LEFT)
#         self.state_entry = ttk.Entry(state_frame, width=10)
#         self.state_entry.pack(side=tk.LEFT, padx=10)
#         ttk.Button(state_frame, text="Analyze State", command=self.analyze_state).pack(side=tk.LEFT)
        

#         self.weather_details_frame = ttk.LabelFrame(self.left_frame, text="Weather Details", padding=10)
#         self.weather_details_frame.pack(fill=tk.BOTH, expand=True)
        

#         self.plot_frame = ttk.LabelFrame(self.right_frame, text="Weather Comparisons", padding=10)
#         self.plot_frame.pack(fill=tk.BOTH, expand=True)
        

#         self.status_label = ttk.Label(self.root, text="", foreground="red", style='SubHeader.TLabel')
#         self.status_label.pack(fill=tk.X, padx=20, pady=5)
        
#     def create_weather_card(self, data):

#         for widget in self.weather_details_frame.winfo_children():
#             widget.destroy()
            

#         card = ttk.Frame(self.weather_details_frame, style='Card.TFrame', padding=10)
#         card.pack(fill=tk.X, pady=5, padx=5)
        

#         ttk.Label(card, text=f"{data['City']}", style='Header.TLabel').pack(pady=(0, 10))
#         ttk.Label(card, text=f"Current Conditions: {data['Weather Condition']}", style='SubHeader.TLabel').pack()
        

#         details_frame = ttk.Frame(card)
#         details_frame.pack(fill=tk.X, pady=10)
        

#         temp_frame = ttk.Frame(details_frame)
#         temp_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(temp_frame, text=f"Temperature: {data['Temperature (°C)']}°C", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
#         ttk.Label(temp_frame, text=f"Humidity: {data['Humidity (%)']}%", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        

#         wind_frame = ttk.Frame(details_frame)
#         wind_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(wind_frame, text=f"Wind Speed: {data['Wind Speed (m/s)']} m/s", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
#         ttk.Label(wind_frame, text=f"Air Quality Index: {data.get('AQI', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        

#         sun_frame = ttk.Frame(details_frame)
#         sun_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(sun_frame, text=f"Sunrise: {data.get('Sunrise', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
#         ttk.Label(sun_frame, text=f"Sunset: {data.get('Sunset', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        

#         if data.get('Alerts', 'None') != 'None':
#             alert_frame = ttk.Frame(card)
#             alert_frame.pack(fill=tk.X, pady=10)
#             ttk.Label(alert_frame, text="Weather Alerts:", style='SubHeader.TLabel', foreground='red').pack()
#             ttk.Label(alert_frame, text=data['Alerts'], style='Data.TLabel', wraplength=400).pack(pady=5)

#     def fetch_central_city_data(self):
#         city = self.central_city_entry.get().strip()
#         if not city:
#             self.show_error("Please enter a city name")
#             return
            
#         self.central_city_data = self.get_weather_data(self.DEFAULT_API_KEY, city)
#         if self.central_city_data:
#             self.create_weather_card(self.central_city_data)
            
#     def analyze_state(self):
#         state = self.state_entry.get().strip()
#         if not state:
#             self.show_error("Please enter a state code")
#             return
            
#         cities_in_state = self.get_cities_in_state(state)
#         if not cities_in_state:
#             self.show_error(f"No cities found for {state}")
#             return
            
#         self.state_cities_data = []
#         for city in cities_in_state:
#             weather = self.get_weather_data(self.DEFAULT_API_KEY, f"{city},{state},US")
#             if weather:
#                 self.state_cities_data.append(weather)
        
#         if self.state_cities_data:
#             self.update_plots()
#             self.show_state_analysis_summary()
            
#     def get_cities_in_state(self, state):
#         state_city_map = {
#             "AP": ["Visakhapatnam", "Vijayawada", "Guntur", "Tirupati", "Rajahmundry", "Kakinada", "Nellore", "Anantapur", "Kadapa", "Srikakulam"],
#             "AR": ["Itanagar", "Naharlagun", "Tawang", "Ziro", "Bomdila", "Pasighat", "Roing", "Tezu", "Changlang", "Daporijo"],
#             "AS": ["Guwahati", "Dibrugarh", "Silchar", "Jorhat", "Tezpur", "Nagaon", "Tinsukia", "Barpeta", "Sivasagar", "Bongaigaon"],
#             "BR": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur", "Darbhanga", "Bihar Sharif", "Ara", "Begusarai", "Purnia", "Chapra"],
#             "CG": ["Raipur", "Bhilai", "Bilaspur", "Durg", "Korba", "Rajnandgaon", "Jagdalpur", "Raigarh", "Ambikapur", "Kanker"],
#             "GA": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda", "Bicholim", "Curchorem", "Canacona", "Sanguem", "Valpoi"],
#             "GJ": ["Ahmedabad", "Surat", "Vadodara", "Gandhinagar", "Mehsana", "Rajkot", "Bhavnagar", "Jamnagar", "Anand", "Junagadh"],
#             "HR": ["Gurugram", "Faridabad", "Panipat", "Ambala", "Yamunanagar", "Rohtak", "Hisar", "Karnal", "Sonipat", "Panchkula"],
#             "HP": ["Shimla", "Manali", "Dharamshala", "Solan", "Mandi", "Kullu", "Chamba", "Una", "Hamirpur", "Bilaspur"],
#             "JH": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh", "Deoghar", "Giridih", "Ramgarh", "Medininagar", "Chaibasa"],
#             "KA": ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru", "Belagavi", "Shivamogga", "Davanagere", "Ballari", "Bidar", "Udupi"],
#             "KL": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Alappuzha", "Kollam", "Palakkad", "Kannur", "Kottayam", "Malappuram"],
#             "MP": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain", "Sagar", "Rewa", "Satna", "Ratlam", "Chhindwara"],
#             "MH": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Amravati", "Kolhapur", "Latur", "Jalgaon"],
#             "MN": ["Imphal", "Thoubal", "Bishnupur", "Churachandpur", "Kakching", "Senapati", "Ukhrul", "Tamenglong", "Jiribam", "Moirang"],
#             "ML": ["Shillong", "Tura", "Nongstoin", "Jowai", "Baghmara", "Resubelpara", "Williamnagar", "Mairang", "Khliehriat", "Ampati"],
#             "MZ": ["Aizawl", "Lunglei", "Saiha", "Champhai", "Serchhip", "Kolasib", "Lawngtlai", "Mamit", "Bairabi", "Saitual"],
#             "NL": ["Kohima", "Dimapur", "Mokokchung", "Tuensang", "Wokha", "Zunheboto", "Mon", "Phek", "Kiphire", "Longleng"],
#             "OR": ["Bhubaneswar", "Cuttack", "Rourkela", "Puri", "Sambalpur", "Berhampur", "Balasore", "Jharsuguda", "Angul", "Koraput"],
#             "PB": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Mohali", "Hoshiarpur", "Pathankot", "Firozpur", "Sangrur"],
#             "RJ": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner", "Ajmer", "Bharatpur", "Alwar", "Sikar", "Chittorgarh"],
#             "SK": ["Gangtok", "Namchi", "Gyalshing", "Mangan", "Rangpo", "Jorethang", "Singtam", "Pakyong", "Soreng", "Ravangla"],
#             "TN": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Vellore", "Erode", "Thoothukudi", "Kanchipuram"],
#             "TS": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam", "Mahbubnagar", "Ramagundam", "Adilabad", "Siddipet", "Nalgonda"],
#             "TR": ["Agartala", "Udaipur", "Dharmanagar", "Kailashahar", "Belonia", "Ambassa", "Khowai", "Sonamura", "Melaghar", "Ranirbazar"],
#             "UP": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Meerut", "Prayagraj", "Ghaziabad", "Bareilly", "Aligarh", "Moradabad"],
#             "UK": ["Dehradun", "Haridwar", "Nainital", "Haldwani", "Rishikesh", "Roorkee", "Kashipur", "Rudrapur", "Pithoragarh", "Mussoorie"],
#             "WB": ["Kolkata", "Howrah", "Durgapur", "Siliguri", "Asansol", "Bardhaman", "Kharagpur", "Malda", "Jalpaiguri", "Bankura"]
#         }

#         return state_city_map.get(state.upper(), [])
            
#     def get_weather_data(self, api_key, location):
#         try:
#             params = {'q': location, 'appid': api_key, 'units': 'metric'}
#             response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
#             response.raise_for_status()
#             data = response.json()
            
#             aqi = self.get_air_quality(api_key, data['coord']['lat'], data['coord']['lon'])
#             sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
#             sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
#             alerts = self.get_weather_alerts(api_key, data['id'])
            
#             return {
#                 'City': data['name'],
#                 'Temperature (°C)': data['main']['temp'],
#                 'Humidity (%)': data['main']['humidity'],
#                 'Wind Speed (m/s)': data['wind']['speed'],
#                 'Weather Condition': data['weather'][0]['main'],
#                 'AQI': aqi,
#                 'Sunrise': sunrise,
#                 'Sunset': sunset,
#                 'Alerts': alerts
#             }
#         except Exception as e:
#             self.show_error(f"Error fetching data for {location}: {str(e)}")
#             return None
            
#     def get_air_quality(self, api_key, lat, lon):
#         try:
#             params = {'lat': lat, 'lon': lon, 'appid': api_key}
#             response = requests.get("http://api.openweathermap.org/data/2.5/air_pollution", params=params)
#             response.raise_for_status()
#             return response.json()['list'][0]['main']['aqi']
#         except:
#             return "N/A"
            
#     def get_weather_alerts(self, api_key, city_id):
#         try:
#             params = {'id': city_id, 'appid': api_key, 'exclude': 'current,minutely,hourly,daily'}
#             response = requests.get("http://api.openweathermap.org/data/2.5/onecall", params=params)
#             response.raise_for_status()
#             alerts = response.json().get('alerts', [])
#             return ", ".join([alert['event'] for alert in alerts]) if alerts else "None"
#         except:
#             return "N/A"
            
#     def update_plots(self):
#         if self.current_figure:
#             for widget in self.plot_frame.winfo_children():
#                 widget.destroy()
                
#         fig = plt.Figure(figsize=(12, 10))
#         axs = fig.subplots(3, 1, sharex=True)  
#         df = pd.DataFrame(self.state_cities_data)
#         cities = df['City']
#         colors=['red','blue','orange','purple','yellow','green','pink','skyblue','brown','black']
#         #  autopct='%1.1f%%'
        
#         temp_bars = axs[0].bar(cities, df['Temperature (°C)'], color=colors)
#         axs[0].set_title('Temperature Comparison', fontsize=16)
#         axs[0].set_ylabel('°C', fontsize=12)
#         axs[0].tick_params(axis='x', rotation=45)
#         self._add_value_labels(axs[0], temp_bars)
        
#         axs[1].plot(cities, df['Humidity (%)'], marker='o', color='lightgreen', linestyle='-')
#         axs[1].set_title('Humidity Comparison', fontsize=16)
#         axs[1].set_ylabel('%', fontsize=12)
#         axs[1].grid(True)

#         axs[1].tick_params(axis='x', rotation=45)
        
#         axs[2].pie(df['Wind Speed (m/s)'], autopct="%1.1f%%")
#         axs[2].set_title('Wind Speed Comparison', fontsize=16)
       
      
        
#         fig.tight_layout(pad=5.0)
#         canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
#         canvas.draw()
#         canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#         self.current_figure = fig
        
#     def _add_value_labels(self, ax, bars):
#         for bar in bars:
#             height = bar.get_height()
#             ax.text(
#                 bar.get_x() + bar.get_width()/2.,
#                 height,
#                 f'{height:.1f}',
#                 ha='center',
#                 va='bottom'
#             )
        
#     def show_state_analysis_summary(self):
#         df = pd.DataFrame(self.state_cities_data)
        
#         for widget in self.weather_details_frame.winfo_children():
#             widget.destroy()
            
#         summary_card = ttk.Frame(self.weather_details_frame, style='Card.TFrame', padding=10)
#         summary_card.pack(fill=tk.X, pady=5, padx=5)
        
#         ttk.Label(summary_card, text="State Weather Analysis Summary", style='Header.TLabel').pack(pady=(0, 10))
        
#         hottest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=True)
#         coldest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=False)
        
#         temp_frame = ttk.Frame(summary_card)
#         temp_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(temp_frame, text="Temperature Analysis", style='SubHeader.TLabel').pack(pady=(5, 0))
#         ttk.Label(temp_frame, text=f"Top 3 Hottest Cities: {', '.join(hottest)}", style='Data.TLabel').pack(pady=2)
#         ttk.Label(temp_frame, text=f"Top 3 Coldest Cities: {', '.join(coldest)}", style='Data.TLabel').pack(pady=2)
        
#         conditions_frame = ttk.Frame(summary_card)
#         conditions_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(conditions_frame, text="Weather Conditions", style='SubHeader.TLabel').pack(pady=(5, 0))
        
#         conditions = df['Weather Condition'].value_counts()
#         for condition, count in conditions.items():
#             ttk.Label(conditions_frame, 
#                      text=f"{condition}: {count} {'city' if count == 1 else 'cities'}", 
#                      style='Data.TLabel').pack(pady=2)
        
#         stats_frame = ttk.Frame(summary_card)
#         stats_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(stats_frame, text="Statistics", style='SubHeader.TLabel').pack(pady=(5, 0))
        
#         avg_temp = df['Temperature (°C)'].mean()
#         avg_humidity = df['Humidity (%)'].mean()
#         avg_wind = df['Wind Speed (m/s)'].mean()
        
#         ttk.Label(stats_frame, text=f"Average Temperature: {avg_temp:.1f}°C", style='Data.TLabel').pack(pady=2)
#         ttk.Label(stats_frame, text=f"Average Humidity: {avg_humidity:.1f}%", style='Data.TLabel').pack(pady=2)
#         ttk.Label(stats_frame, text=f"Average Wind Speed: {avg_wind:.1f} m/s", style='Data.TLabel').pack(pady=2)
        
#     def get_top_cities(self, df, column, n=3, hottest=True):
#         pq = PriorityQueue(is_max=not hottest)
#         for a, row in df.iterrows():
#             pq.push(row[column], row['City'])
#             if pq.size() > n:
#                 pq.pop()
#         sorted_items = pq.get_sorted_items()
#         sorted_items.reverse()
#         return [city for (a, city) in sorted_items]
        
#     def show_error(self, message):
#         self.status_label.config(text=message)
#         self.root.after(5000, lambda: self.status_label.config(text=""))

# if __name__ == "__main__":
#     root = ThemedTk(theme="arc")  
#     app = WeatherAnalysisApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from datetime import datetime
import heapq
from ttkthemes import ThemedTk

class PriorityQueue:
    """A priority queue that supports both min-heap and max-heap behavior."""
    def __init__(self, is_max=False):
        self.heap = []
        self.is_max = is_max

    def push(self, key, value):
        if self.is_max:
            key = -key
        heapq.heappush(self.heap, (key, value))

    def pop(self):
        key, value = heapq.heappop(self.heap)
        if self.is_max:
            key = -key
        return (key, value)

    def size(self):
        return len(self.heap)

    def get_sorted_items(self):
        temp_heap = list(self.heap)
        sorted_items = []
        while temp_heap:
            key, value = heapq.heappop(temp_heap)
            if self.is_max:
                key = -key
            sorted_items.append((key, value))
        sorted_items.sort(reverse=self.is_max)
        return sorted_items

class WeatherAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Analysis Tool")
        self.root.geometry("1400x900")
        
        # Set default API key
        self.DEFAULT_API_KEY = '0b8a3295928677e77622cb04ee7aa299'  # Replace with your actual API key
        
        # Set theme
        self.style = ttk.Style()
        self.style.theme_use('arc')
        
        # Configure styles
        self.style.configure('Header.TLabel', font=('Helvetica', 18, 'bold'))
        self.style.configure('SubHeader.TLabel', font=('Helvetica', 14))
        self.style.configure('Data.TLabel', font=('Helvetica', 12))
        self.style.configure('Card.TFrame', relief='solid', borderwidth=1, background='#f0f0f0')
        
        # Initialize data storage
        self.central_city_data = None
        self.state_cities_data = []
        self.current_figure = None
        
        # Create main containers
        self.create_main_layout()
        self.create_widgets()
        
    def create_main_layout(self):
        # Create main containers
        self.input_frame = ttk.Frame(self.root, padding="20 20 20 10")
        self.input_frame.pack(fill=tk.X)
        
        self.content_frame = ttk.Frame(self.root, padding="20 10 20 20")
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Split content frame into left and right sections
        self.left_frame = ttk.Frame(self.content_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        self.right_frame = ttk.Frame(self.content_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
    def create_widgets(self):
        # Title
        ttk.Label(self.input_frame, text="Weather Analysis Dashboard", style='Header.TLabel').pack(pady=(0, 20))
        
        # Input Controls Frame
        controls_frame = ttk.LabelFrame(self.input_frame, text="Controls", padding=10)
        controls_frame.pack(fill=tk.X)
        
        # City Input Section
        input_frame = ttk.Frame(controls_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        # Central City
        central_frame = ttk.Frame(input_frame)
        central_frame.pack(side=tk.LEFT, padx=(0, 20))
        ttk.Label(central_frame, text="Central City:", style='SubHeader.TLabel').pack(side=tk.LEFT)
        self.central_city_entry = ttk.Entry(central_frame, width=20)
        self.central_city_entry.pack(side=tk.LEFT, padx=10)
        ttk.Button(central_frame, text="Fetch Data", command=self.fetch_central_city_data).pack(side=tk.LEFT)
        
        # State Analysis
        state_frame = ttk.Frame(input_frame)
        state_frame.pack(side=tk.LEFT)
        ttk.Label(state_frame, text="State Code:", style='SubHeader.TLabel').pack(side=tk.LEFT)
        self.state_entry = ttk.Entry(state_frame, width=10)
        self.state_entry.pack(side=tk.LEFT, padx=10)
        ttk.Button(state_frame, text="Analyze State", command=self.analyze_state).pack(side=tk.LEFT)
        
        # Create weather details frame in left section
        self.weather_details_frame = ttk.LabelFrame(self.left_frame, text="Weather Details", padding=10)
        self.weather_details_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create plots frame in right section
        self.plot_frame = ttk.LabelFrame(self.right_frame, text="Weather Comparisons", padding=10)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status Label
        self.status_label = ttk.Label(self.root, text="", foreground="red", style='SubHeader.TLabel')
        self.status_label.pack(fill=tk.X, padx=20, pady=5)
        
    def create_weather_card(self, data):
        # Clear previous data
        for widget in self.weather_details_frame.winfo_children():
            widget.destroy()
            
        # Create a card-like frame
        card = ttk.Frame(self.weather_details_frame, style='Card.TFrame', padding=10)
        card.pack(fill=tk.X, pady=5, padx=5)
        
        # City name and current conditions
        ttk.Label(card, text=f"{data['City']}", style='Header.TLabel').pack(pady=(0, 10))
        ttk.Label(card, text=f"Current Conditions: {data['Weather Condition']}", style='SubHeader.TLabel').pack()
        
        # Create grid for details
        details_frame = ttk.Frame(card)
        details_frame.pack(fill=tk.X, pady=10)
        
        # Temperature and humidity
        temp_frame = ttk.Frame(details_frame)
        temp_frame.pack(fill=tk.X, pady=5)
        ttk.Label(temp_frame, text=f"Temperature: {data['Temperature (°C)']}°C", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        ttk.Label(temp_frame, text=f"Humidity: {data['Humidity (%)']}%", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        
        # Wind and AQI
        wind_frame = ttk.Frame(details_frame)
        wind_frame.pack(fill=tk.X, pady=5)
        ttk.Label(wind_frame, text=f"Wind Speed: {data['Wind Speed (m/s)']} m/s", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        ttk.Label(wind_frame, text=f"Air Quality Index: {data.get('AQI', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        
        # Sun times
        sun_frame = ttk.Frame(details_frame)
        sun_frame.pack(fill=tk.X, pady=5)
        ttk.Label(sun_frame, text=f"Sunrise: {data.get('Sunrise', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        ttk.Label(sun_frame, text=f"Sunset: {data.get('Sunset', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        
        # Alerts
        if data.get('Alerts', 'None') != 'None':
            alert_frame = ttk.Frame(card)
            alert_frame.pack(fill=tk.X, pady=10)
            ttk.Label(alert_frame, text="Weather Alerts:", style='SubHeader.TLabel', foreground='red').pack()
            ttk.Label(alert_frame, text=data['Alerts'], style='Data.TLabel', wraplength=400).pack(pady=5)

    def fetch_central_city_data(self):
        city = self.central_city_entry.get().strip()
        if not city:
            self.show_error("Please enter a city name")
            return
            
        self.central_city_data = self.get_weather_data(self.DEFAULT_API_KEY, city)
        if self.central_city_data:
            self.create_weather_card(self.central_city_data)
            
    def analyze_state(self):
        state = self.state_entry.get().strip()
        if not state:
            self.show_error("Please enter a state code")
            return
            
        cities_in_state = self.get_cities_in_state(state)
        if not cities_in_state:
            self.show_error(f"No cities found for {state}")
            return
            
        self.state_cities_data = []
        for city in cities_in_state:
            weather = self.get_weather_data(self.DEFAULT_API_KEY, f"{city},{state},US")
            if weather:
                self.state_cities_data.append(weather)
        
        if self.state_cities_data:
            self.update_plots()
            self.show_state_analysis_summary()
            
    def get_cities_in_state(self, state):
        state_city_map = {
            "CA": ["Los Angeles", "San Francisco", "San Diego", "Sacramento"],
            "NY": ["New York", "Buffalo", "Albany", "Rochester"],
            "TX": ["Houston", "Dallas", "Austin", "San Antonio"],
            "GJ": ["Ahmedabad","Surat","Baroda","Gandhinagar","Mehsana"]
        }
        return state_city_map.get(state.upper(), [])
            
    def get_weather_data(self, api_key, location):
        try:
            params = {'q': location, 'appid': api_key, 'units': 'metric'}
            response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
            response.raise_for_status()
            data = response.json()
            
            aqi = self.get_air_quality(api_key, data['coord']['lat'], data['coord']['lon'])
            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
            alerts = self.get_weather_alerts(api_key, data['id'])
            
            return {
                'City': data['name'],
                'Temperature (°C)': data['main']['temp'],
                'Humidity (%)': data['main']['humidity'],
                'Wind Speed (m/s)': data['wind']['speed'],
                'Weather Condition': data['weather'][0]['main'],
                'AQI': aqi,
                'Sunrise': sunrise,
                'Sunset': sunset,
                'Alerts': alerts
            }
        except Exception as e:
            self.show_error(f"Error fetching data for {location}: {str(e)}")
            return None
            
    def get_air_quality(self, api_key, lat, lon):
        try:
            params = {'lat': lat, 'lon': lon, 'appid': api_key}
            response = requests.get("http://api.openweathermap.org/data/2.5/air_pollution", params=params)
            response.raise_for_status()
            return response.json()['list'][0]['main']['aqi']
        except:
            return "N/A"
            
    def get_weather_alerts(self, api_key, city_id):
        try:
            params = {'id': city_id, 'appid': api_key, 'exclude': 'current,minutely,hourly,daily'}
            response = requests.get("http://api.openweathermap.org/data/2.5/onecall", params=params)
            response.raise_for_status()
            alerts = response.json().get('alerts', [])
            return ", ".join([alert['event'] for alert in alerts]) if alerts else "None"
        except:
            return "N/A"
            
    def update_plots(self):
        if self.current_figure:
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
                
        fig = plt.Figure(figsize=(12, 10))
        axs = fig.subplots(3, 1)
        df = pd.DataFrame(self.state_cities_data)
        cities = df['City']
        
        # Temperature plot (Bar Graph)
        temp_bars = axs[0].bar(cities, df['Temperature (°C)'], color='skyblue')
        axs[0].set_title('Temperature Comparison')
        axs[0].set_ylabel('°C')
        axs[0].tick_params(axis='x', rotation=45)
        self._add_value_labels(axs[0], temp_bars)
        
        # Humidity plot (Line Graph)
        axs[1].plot(cities, df['Humidity (%)'], marker='o', color='lightgreen', linestyle='-')
        axs[1].set_title('Humidity Comparison')
        axs[1].set_ylabel('%')
        axs[1].tick_params(axis='x', rotation=45)
        
        # Wind speed plot (Scatter Plot)
        axs[2].scatter(cities, df['Wind Speed (m/s)'], color='salmon')
        axs[2].set_title('Wind Speed Comparison')
        axs[2].set_ylabel('m/s')
        axs[2].tick_params(axis='x', rotation=45)
        
        fig.tight_layout(pad=3.0)
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.current_figure = fig
        
    def _add_value_labels(self, ax, bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2.,
                height,
                f'{height:.1f}',
                ha='center',
                va='bottom'
            )
        
    def show_state_analysis_summary(self):
        df = pd.DataFrame(self.state_cities_data)
        
        # Create summary card
        for widget in self.weather_details_frame.winfo_children():
            widget.destroy()
            
        summary_card = ttk.Frame(self.weather_details_frame, style='Card.TFrame', padding=10)
        summary_card.pack(fill=tk.X, pady=5, padx=5)
        
        # Title
        ttk.Label(summary_card, text="State Weather Analysis Summary", style='Header.TLabel').pack(pady=(0, 10))
        
        # Get top cities using PriorityQueue
        hottest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=True)
        coldest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=False)
        
        # Temperature analysis
        temp_frame = ttk.Frame(summary_card)
        temp_frame.pack(fill=tk.X, pady=5)
        ttk.Label(temp_frame, text="Temperature Analysis", style='SubHeader.TLabel').pack(pady=(5, 0))
        ttk.Label(temp_frame, text=f"Top 3 Hottest Cities: {', '.join(hottest)}", style='Data.TLabel').pack(pady=2)
        ttk.Label(temp_frame, text=f"Top 3 Coldest Cities: {', '.join(coldest)}", style='Data.TLabel').pack(pady=2)
        
        # Weather conditions summary
        conditions_frame = ttk.Frame(summary_card)
        conditions_frame.pack(fill=tk.X, pady=5)
        ttk.Label(conditions_frame, text="Weather Conditions", style='SubHeader.TLabel').pack(pady=(5, 0))
        
        # Count weather conditions
        conditions = df['Weather Condition'].value_counts()
        for condition, count in conditions.items():
            ttk.Label(conditions_frame, 
                     text=f"{condition}: {count} {'city' if count == 1 else 'cities'}", 
                     style='Data.TLabel').pack(pady=2)
        
        # Statistics
        stats_frame = ttk.Frame(summary_card)
        stats_frame.pack(fill=tk.X, pady=5)
        ttk.Label(stats_frame, text="Statistics", style='SubHeader.TLabel').pack(pady=(5, 0))
        
        avg_temp = df['Temperature (°C)'].mean()
        avg_humidity = df['Humidity (%)'].mean()
        avg_wind = df['Wind Speed (m/s)'].mean()
        
        ttk.Label(stats_frame, text=f"Average Temperature: {avg_temp:.1f}°C", style='Data.TLabel').pack(pady=2)
        ttk.Label(stats_frame, text=f"Average Humidity: {avg_humidity:.1f}%", style='Data.TLabel').pack(pady=2)
        ttk.Label(stats_frame, text=f"Average Wind Speed: {avg_wind:.1f} m/s", style='Data.TLabel').pack(pady=2)
        
    def get_top_cities(self, df, column, n=3, hottest=True):
        pq = PriorityQueue(is_max=not hottest)
        for _, row in df.iterrows():
            pq.push(row[column], row['City'])
            if pq.size() > n:
                pq.pop()
        sorted_items = pq.get_sorted_items()
        sorted_items.reverse()
        return [city for (_, city) in sorted_items]
        
    def show_error(self, message):
        self.status_label.config(text=message)
        self.root.after(5000, lambda: self.status_label.config(text=""))

if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Using ThemedTk for better default styling
    app = WeatherAnalysisApp(root)
    root.mainloop()