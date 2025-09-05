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
#     """A priority queue that supports both min-heap and max-heap behavior."""
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
#         self.root.title("Weather Analysis Tool")
#         self.root.geometry("1400x900")
        
#         # Set default API key
#         self.DEFAULT_API_KEY = '0b8a3295928677e77622cb04ee7aa299'  # Replace with your actual API key
        
#         # Set theme
#         self.style = ttk.Style()
#         self.style.theme_use('arc')
        
#         # Configure styles
#         self.style.configure('Header.TLabel', font=('Helvetica', 18, 'bold'))
#         self.style.configure('SubHeader.TLabel', font=('Helvetica', 14))
#         self.style.configure('Data.TLabel', font=('Helvetica', 12))
#         self.style.configure('Card.TFrame', relief='solid', borderwidth=1, background='#f0f0f0')
        
#         # Initialize data storage
#         self.central_city_data = None
#         self.state_cities_data = []
#         self.current_figure = None
        
#         # Create main containers
#         self.create_main_layout()
#         self.create_widgets()
        
#     def create_main_layout(self):
#         # Create main containers
#         self.input_frame = ttk.Frame(self.root, padding="20 20 20 10")
#         self.input_frame.pack(fill=tk.X)
        
#         self.content_frame = ttk.Frame(self.root, padding="20 10 20 20")
#         self.content_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Split content frame into left and right sections
#         self.left_frame = ttk.Frame(self.content_frame)
#         self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
#         self.right_frame = ttk.Frame(self.content_frame)
#         self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
#     def create_widgets(self):
#         # Title
#         ttk.Label(self.input_frame, text="Weather Analysis Dashboard", style='Header.TLabel').pack(pady=(0, 20))
        
#         # Input Controls Frame
#         controls_frame = ttk.LabelFrame(self.input_frame, text="Controls", padding=10)
#         controls_frame.pack(fill=tk.X)
        
#         # City Input Section
#         input_frame = ttk.Frame(controls_frame)
#         input_frame.pack(fill=tk.X, pady=10)
        
#         # Central City
#         central_frame = ttk.Frame(input_frame)
#         central_frame.pack(side=tk.LEFT, padx=(0, 20))
#         ttk.Label(central_frame, text="Central City:", style='SubHeader.TLabel').pack(side=tk.LEFT)
#         self.central_city_entry = ttk.Entry(central_frame, width=20)
#         self.central_city_entry.pack(side=tk.LEFT, padx=10)
#         ttk.Button(central_frame, text="Fetch Data", command=self.fetch_central_city_data).pack(side=tk.LEFT)
        
#         # State Analysis
#         state_frame = ttk.Frame(input_frame)
#         state_frame.pack(side=tk.LEFT)
#         ttk.Label(state_frame, text="State Code:", style='SubHeader.TLabel').pack(side=tk.LEFT)
#         self.state_entry = ttk.Entry(state_frame, width=10)
#         self.state_entry.pack(side=tk.LEFT, padx=10)
#         ttk.Button(state_frame, text="Analyze State", command=self.analyze_state).pack(side=tk.LEFT)
        
#         # Create weather details frame in left section
#         self.weather_details_frame = ttk.LabelFrame(self.left_frame, text="Weather Details", padding=10)
#         self.weather_details_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Create plots frame in right section
#         self.plot_frame = ttk.LabelFrame(self.right_frame, text="Weather Comparisons", padding=10)
#         self.plot_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Status Label
#         self.status_label = ttk.Label(self.root, text="", foreground="red", style='SubHeader.TLabel')
#         self.status_label.pack(fill=tk.X, padx=20, pady=5)
        
#     def create_weather_card(self, data):
#         # Clear previous data
#         for widget in self.weather_details_frame.winfo_children():
#             widget.destroy()
            
#         # Create a card-like frame
#         card = ttk.Frame(self.weather_details_frame, style='Card.TFrame', padding=10)
#         card.pack(fill=tk.X, pady=5, padx=5)
        
#         # City name and current conditions
#         ttk.Label(card, text=f"{data['City']}", style='Header.TLabel').pack(pady=(0, 10))
#         ttk.Label(card, text=f"Current Conditions: {data['Weather Condition']}", style='SubHeader.TLabel').pack()
        
#         # Create grid for details
#         details_frame = ttk.Frame(card)
#         details_frame.pack(fill=tk.X, pady=10)
        
#         # Temperature and humidity
#         temp_frame = ttk.Frame(details_frame)
#         temp_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(temp_frame, text=f"Temperature: {data['Temperature (°C)']}°C", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
#         ttk.Label(temp_frame, text=f"Humidity: {data['Humidity (%)']}%", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        
#         # Wind and AQI
#         wind_frame = ttk.Frame(details_frame)
#         wind_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(wind_frame, text=f"Wind Speed: {data['Wind Speed (m/s)']} m/s", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
#         ttk.Label(wind_frame, text=f"Air Quality Index: {data.get('AQI', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        
#         # Sun times
#         sun_frame = ttk.Frame(details_frame)
#         sun_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(sun_frame, text=f"Sunrise: {data.get('Sunrise', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
#         ttk.Label(sun_frame, text=f"Sunset: {data.get('Sunset', 'N/A')}", style='Data.TLabel').pack(side=tk.LEFT, padx=20)
        
#         # Alerts
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
#             "CA": ["Los Angeles", "San Francisco", "San Diego", "Sacramento"],
#             "NY": ["New York", "Buffalo", "Albany", "Rochester"],
#             "TX": ["Houston", "Dallas", "Austin", "San Antonio"],
#             "GJ": ["Ahmedabad","Surat","Baroda","Gandhinagar","Mehsana"]
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
#         axs = fig.subplots(3, 1)
#         df = pd.DataFrame(self.state_cities_data)
#         cities = df['City']
        
#         # Temperature plot (Bar Graph)
#         temp_bars = axs[0].bar(cities, df['Temperature (°C)'], color='skyblue')
#         axs[0].set_title('Temperature Comparison')
#         axs[0].set_ylabel('°C')
#         axs[0].tick_params(axis='x', rotation=45)
#         self._add_value_labels(axs[0], temp_bars)
        
#         # Humidity plot (Line Graph)
#         axs[1].plot(cities, df['Humidity (%)'], marker='o', color='lightgreen', linestyle='-')
#         axs[1].set_title('Humidity Comparison')
#         axs[1].set_ylabel('%')
#         axs[1].tick_params(axis='x', rotation=45)
        
#         # Wind speed plot (Scatter Plot)
#         axs[2].scatter(cities, df['Wind Speed (m/s)'], color='salmon')
#         axs[2].set_title('Wind Speed Comparison')
#         axs[2].set_ylabel('m/s')
#         axs[2].tick_params(axis='x', rotation=45)
        
#         fig.tight_layout(pad=3.0)
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
        
#         # Create summary card
#         for widget in self.weather_details_frame.winfo_children():
#             widget.destroy()
            
#         summary_card = ttk.Frame(self.weather_details_frame, style='Card.TFrame', padding=10)
#         summary_card.pack(fill=tk.X, pady=5, padx=5)
        
#         # Title
#         ttk.Label(summary_card, text="State Weather Analysis Summary", style='Header.TLabel').pack(pady=(0, 10))
        
#         # Get top cities using PriorityQueue
#         hottest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=True)
#         coldest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=False)
        
#         # Temperature analysis
#         temp_frame = ttk.Frame(summary_card)
#         temp_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(temp_frame, text="Temperature Analysis", style='SubHeader.TLabel').pack(pady=(5, 0))
#         ttk.Label(temp_frame, text=f"Top 3 Hottest Cities: {', '.join(hottest)}", style='Data.TLabel').pack(pady=2)
#         ttk.Label(temp_frame, text=f"Top 3 Coldest Cities: {', '.join(coldest)}", style='Data.TLabel').pack(pady=2)
        
#         # Weather conditions summary
#         conditions_frame = ttk.Frame(summary_card)
#         conditions_frame.pack(fill=tk.X, pady=5)
#         ttk.Label(conditions_frame, text="Weather Conditions", style='SubHeader.TLabel').pack(pady=(5, 0))
        
#         # Count weather conditions
#         conditions = df['Weather Condition'].value_counts()
#         for condition, count in conditions.items():
#             ttk.Label(conditions_frame, 
#                      text=f"{condition}: {count} {'city' if count == 1 else 'cities'}", 
#                      style='Data.TLabel').pack(pady=2)
        
#         # Statistics
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
#         for _, row in df.iterrows():
#             pq.push(row[column], row['City'])
#             if pq.size() > n:
#                 pq.pop()
#         sorted_items = pq.get_sorted_items()
#         sorted_items.reverse()
#         return [city for (_, city) in sorted_items]
        
#     def show_error(self, message):
#         self.status_label.config(text=message)
#         self.root.after(5000, lambda: self.status_label.config(text=""))

# if __name__ == "__main__":
#     root = ThemedTk(theme="arc")  # Using ThemedTk for better default styling
#     app = WeatherAnalysisApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import ttk
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from datetime import datetime
import heapq


class PriorityQueue:
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


class WeatherAnalysisCarouselApp:
    def __init__(self, root):
        self.root = root
        self.root.title("☀️ Weather Analysis Carousel Dashboard")
        self.root.geometry("1500x900")
        self.root.configure(bg="#f8f9fa")
        
        self.DEFAULT_API_KEY = '0b8a3295928677e77622cb04ee7aa299'
        
        # Data storage
        self.central_city_data = None
        self.state_cities_data = []
        self.current_figures = []
        self.current_canvas = None
        self.current_index = 0
        self.chart_titles = []
        
        self.configure_styles()
        self.create_main_layout()
        self.create_widgets()

    def configure_styles(self):
        """Configure clean light theme styling"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.colors = {
            'bg_main': '#f8f9fa',
            'bg_card': '#ffffff',
            'bg_accent': '#e9ecef',
            'primary': '#007bff',
            'secondary': '#6c757d',
            'success': '#28a745',
            'warning': '#ffc107',
            'danger': '#dc3545',
            'text_dark': '#212529',
            'text_muted': '#6c757d'
        }
        
        # Style configurations
        self.style.configure('Title.TLabel', 
                           font=('Segoe UI', 28, 'bold'), 
                           foreground=self.colors['primary'], 
                           background=self.colors['bg_main'])
        
        self.style.configure('Header.TLabel', 
                           font=('Segoe UI', 20, 'bold'), 
                           foreground=self.colors['text_dark'], 
                           background=self.colors['bg_card'])
        
        self.style.configure('SubHeader.TLabel', 
                           font=('Segoe UI', 16, 'bold'), 
                           foreground=self.colors['primary'], 
                           background=self.colors['bg_card'])
        
        self.style.configure('Data.TLabel', 
                           font=('Segoe UI', 14), 
                           foreground=self.colors['text_dark'], 
                           background=self.colors['bg_card'])
        
        self.style.configure('Card.TFrame', 
                           relief='solid', 
                           borderwidth=1,
                           background=self.colors['bg_card'])
        
        self.style.configure('Main.TFrame', 
                           background=self.colors['bg_main'])
        
        self.style.configure('Modern.TLabelframe', 
                           background=self.colors['bg_main'], 
                           foreground=self.colors['primary'],
                           borderwidth=2,
                           relief='solid')
        
        self.style.configure('Modern.TLabelframe.Label', 
                           font=('Segoe UI', 18, 'bold'),
                           background=self.colors['bg_main'], 
                           foreground=self.colors['primary'])
        
        self.style.configure('Primary.TButton', 
                           font=('Segoe UI', 12, 'bold'),
                           background=self.colors['primary'], 
                           foreground='white')
        
        self.style.configure('Carousel.TButton', 
                           font=('Segoe UI', 14, 'bold'),
                           background=self.colors['secondary'], 
                           foreground='white')
        
        self.style.map('Primary.TButton',
                      background=[('active', '#0056b3')])
        
        self.style.map('Carousel.TButton',
                      background=[('active', '#545b62')])
        
        self.style.configure('Modern.TEntry', 
                           font=('Segoe UI', 12),
                           fieldbackground='white',
                           borderwidth=2,
                           relief='solid')

    def create_main_layout(self):
        """Create main layout with proper spacing"""
        # Header
        self.header_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        self.header_frame.pack(fill=tk.X, padx=30, pady=25)
        
        # Main content
        self.main_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))
        
        # Left panel (weather details)
        self.left_panel = tk.Frame(self.main_frame, bg=self.colors['bg_main'])
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        # Right panel (charts with carousel)
        self.right_panel = tk.Frame(self.main_frame, bg=self.colors['bg_main'])
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))

    def create_widgets(self):
        """Create all GUI widgets"""
        # Title section
        title_frame = tk.Frame(self.header_frame, bg=self.colors['bg_main'])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(title_frame, 
                              text="☀️ Weather Analysis Carousel Dashboard", 
                              style='Title.TLabel')
        title_label.pack()
        
        subtitle = tk.Label(title_frame, 
                           text="Interactive weather visualization with carousel navigation",
                           font=('Segoe UI', 14),
                           fg=self.colors['text_muted'], 
                           bg=self.colors['bg_main'])
        subtitle.pack(pady=(5, 0))
        
        # Controls section
        controls_frame = ttk.LabelFrame(self.header_frame, 
                                      text="  Analysis Controls  ", 
                                      padding=20, 
                                      style='Modern.TLabelframe')
        controls_frame.pack(fill=tk.X)
        
        # City analysis row
        city_row = tk.Frame(controls_frame, bg=self.colors['bg_main'])
        city_row.pack(fill=tk.X, pady=(0, 15))
        
        city_label = tk.Label(city_row, text="🏙️ City Analysis", 
                             font=('Segoe UI', 16, 'bold'),
                             fg=self.colors['text_dark'], 
                             bg=self.colors['bg_main'])
        city_label.pack(side=tk.LEFT)
        
        city_input_frame = tk.Frame(city_row, bg=self.colors['bg_main'])
        city_input_frame.pack(side=tk.RIGHT)
        
        tk.Label(city_input_frame, text="City name:", 
                font=('Segoe UI', 12),
                fg=self.colors['text_muted'], 
                bg=self.colors['bg_main']).pack(side=tk.LEFT, padx=(0, 10))
        
        self.central_city_entry = ttk.Entry(city_input_frame, width=25, style='Modern.TEntry')
        self.central_city_entry.pack(side=tk.LEFT, padx=(0, 15))
        
        fetch_btn = ttk.Button(city_input_frame, text="Get Weather", 
                             command=self.fetch_central_city_data,
                             style='Primary.TButton')
        fetch_btn.pack(side=tk.LEFT)
        
        # Separator
        separator = tk.Frame(controls_frame, height=1, bg=self.colors['bg_accent'])
        separator.pack(fill=tk.X, pady=8)
        
        # State analysis row
        state_row = tk.Frame(controls_frame, bg=self.colors['bg_main'])
        state_row.pack(fill=tk.X)
        
        state_label = tk.Label(state_row, text="🗺️ State Analysis", 
                              font=('Segoe UI', 16, 'bold'),
                              fg=self.colors['text_dark'], 
                              bg=self.colors['bg_main'])
        state_label.pack(side=tk.LEFT)
        
        state_input_frame = tk.Frame(state_row, bg=self.colors['bg_main'])
        state_input_frame.pack(side=tk.RIGHT)
        
        tk.Label(state_input_frame, text="State code (MH, KA, etc.):", 
                font=('Segoe UI', 12),
                fg=self.colors['text_muted'], 
                bg=self.colors['bg_main']).pack(side=tk.LEFT, padx=(0, 10))
        
        self.state_entry = ttk.Entry(state_input_frame, width=15, style='Modern.TEntry')
        self.state_entry.pack(side=tk.LEFT, padx=(0, 15))
        
        analyze_btn = ttk.Button(state_input_frame, text="Analyze State", 
                               command=self.analyze_state,
                               style='Primary.TButton')
        analyze_btn.pack(side=tk.LEFT)
        
        # Weather details panel
        self.weather_details_frame = ttk.LabelFrame(self.left_panel, 
                                                  text="  Weather Information  ", 
                                                  padding=20, 
                                                  style='Modern.TLabelframe')
        self.weather_details_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initial welcome message
        self.create_welcome_message()
        
        # Charts panel with carousel controls
        charts_container = tk.Frame(self.right_panel, bg=self.colors['bg_main'])
        charts_container.pack(fill=tk.BOTH, expand=True)
        
        # Carousel controls at top
        self.carousel_controls = tk.Frame(charts_container, bg=self.colors['bg_main'])
        self.carousel_controls.pack(fill=tk.X, pady=(0, 15))
        
        # Navigation buttons
        nav_frame = tk.Frame(self.carousel_controls, bg=self.colors['bg_main'])
        nav_frame.pack(side=tk.LEFT)
        
        self.prev_btn = ttk.Button(nav_frame, text="← Previous", 
                                  command=self.show_prev_plot,
                                  style='Carousel.TButton')
        self.prev_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.next_btn = ttk.Button(nav_frame, text="Next →", 
                                  command=self.show_next_plot,
                                  style='Carousel.TButton')
        self.next_btn.pack(side=tk.LEFT)
        
        # Chart indicator
        self.chart_indicator = tk.Label(self.carousel_controls, 
                                       text="No charts available", 
                                       font=('Segoe UI', 12, 'bold'),
                                       fg=self.colors['text_muted'], 
                                       bg=self.colors['bg_main'])
        self.chart_indicator.pack(side=tk.RIGHT)
        
        # Charts display area
        self.plot_frame = ttk.LabelFrame(charts_container, 
                                       text="  Weather Visualizations  ", 
                                       padding=20, 
                                       style='Modern.TLabelframe')
        self.plot_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initial chart message
        self.create_chart_welcome_message()
        
        # Status bar
        status_frame = tk.Frame(self.root, bg=self.colors['bg_accent'], height=35)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, text="Ready to analyze weather data", 
                                   font=('Segoe UI', 12),
                                   fg=self.colors['success'], 
                                   bg=self.colors['bg_accent'])
        self.status_label.pack(expand=True)

    def create_welcome_message(self):
        """Create welcome message for weather details panel"""
        welcome_frame = tk.Frame(self.weather_details_frame, bg=self.colors['bg_card'])
        welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        welcome_label = tk.Label(welcome_frame, 
                               text="👋 Welcome to Weather Analysis!\n\n" +
                                    "• Enter a city name to get detailed weather information\n" +
                                    "• Analyze weather patterns across multiple cities in a state\n" +
                                    "• Use carousel navigation to browse through different charts",
                               font=('Segoe UI', 14),
                               fg=self.colors['text_muted'], 
                               bg=self.colors['bg_card'],
                               justify=tk.LEFT)
        welcome_label.pack(expand=True, padx=20)

    def create_chart_welcome_message(self):
        """Create welcome message for charts panel"""
        chart_welcome = tk.Label(self.plot_frame, 
                               text="📊 Interactive Weather Charts\n\n" +
                                    "Analyze a state to see comparative weather visualizations:\n" +
                                    "• Temperature comparison across cities\n" +
                                    "• Humidity trends and patterns\n" +
                                    "• Wind speed distribution\n" +
                                    "• Weather conditions breakdown\n\n" +
                                    "Use the carousel buttons to navigate between charts!",
                               font=('Segoe UI', 14),
                               fg=self.colors['text_muted'], 
                               bg=self.colors['bg_card'],
                               justify=tk.LEFT)
        chart_welcome.pack(expand=True)

    def create_weather_card(self, data):
        """Create detailed weather information card"""
        # Clear existing content
        for widget in self.weather_details_frame.winfo_children():
            widget.destroy()

        # Main card
        card = tk.Frame(self.weather_details_frame, bg=self.colors['bg_card'])
        card.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # City header
        header_frame = tk.Frame(card, bg=self.colors['bg_card'])
        header_frame.pack(fill=tk.X, pady=(0, 20))

        city_label = tk.Label(header_frame, text=f"📍 {data['City']}", 
                             font=('Segoe UI', 24, 'bold'),
                             fg=self.colors['text_dark'], 
                             bg=self.colors['bg_card'])
        city_label.pack()

        condition_label = tk.Label(header_frame, 
                                  text=f"{data['Weather Condition']}", 
                                  font=('Segoe UI', 16),
                                  fg=self.colors['primary'], 
                                  bg=self.colors['bg_card'])
        condition_label.pack(pady=(5, 0))

        # Weather metrics in clean grid
        metrics_frame = tk.Frame(card, bg=self.colors['bg_card'])
        metrics_frame.pack(fill=tk.X, pady=20)

        metrics = [
            ("🌡️", "Temperature", f"{data['Temperature (°C)']}°C"),
            ("💧", "Humidity", f"{data['Humidity (%)']}%"),
            ("💨", "Wind Speed", f"{data['Wind Speed (m/s)']} m/s"),
            ("🌫️", "Air Quality", f"AQI {data.get('AQI', 'N/A')}")
        ]

        for i, (icon, label, value) in enumerate(metrics):
            row = i // 2
            col = i % 2
            
            metric_frame = tk.Frame(metrics_frame, bg=self.colors['bg_card'])
            metric_frame.grid(row=row, column=col, padx=25, pady=15, sticky="w")
            
            icon_label = tk.Label(metric_frame, text=icon, 
                                 font=('Segoe UI', 20),
                                 bg=self.colors['bg_card'])
            icon_label.pack(side=tk.LEFT, padx=(0, 15))
            
            text_frame = tk.Frame(metric_frame, bg=self.colors['bg_card'])
            text_frame.pack(side=tk.LEFT)
            
            tk.Label(text_frame, text=label, 
                    font=('Segoe UI', 12),
                    fg=self.colors['text_muted'], 
                    bg=self.colors['bg_card']).pack(anchor="w")
            
            tk.Label(text_frame, text=value, 
                    font=('Segoe UI', 16, 'bold'),
                    fg=self.colors['text_dark'], 
                    bg=self.colors['bg_card']).pack(anchor="w")

        # Sun times if available
        if data.get('Sunrise') != 'N/A' and data.get('Sunset') != 'N/A':
            sun_frame = tk.Frame(card, bg=self.colors['bg_accent'])
            sun_frame.pack(fill=tk.X, pady=(20, 0), padx=10)
            
            tk.Label(sun_frame, text="☀️ Sun Times", 
                    font=('Segoe UI', 14, 'bold'),
                    fg=self.colors['text_dark'], 
                    bg=self.colors['bg_accent']).pack(pady=12)
            
            times_frame = tk.Frame(sun_frame, bg=self.colors['bg_accent'])
            times_frame.pack(pady=(0, 12))
            
            tk.Label(times_frame, text=f"🌅 Sunrise: {data.get('Sunrise', 'N/A')}", 
                    font=('Segoe UI', 12),
                    fg=self.colors['text_dark'], 
                    bg=self.colors['bg_accent']).pack(side=tk.LEFT, padx=25)
            
            tk.Label(times_frame, text=f"🌇 Sunset: {data.get('Sunset', 'N/A')}", 
                    font=('Segoe UI', 12),
                    fg=self.colors['text_dark'], 
                    bg=self.colors['bg_accent']).pack(side=tk.LEFT, padx=25)

    def fetch_central_city_data(self):
        """Fetch weather data for a single city"""
        city = self.central_city_entry.get().strip()
        if not city:
            self.show_status("Please enter a city name", self.colors['danger'])
            return
            
        self.show_status("Fetching weather data...", self.colors['warning'])
        self.central_city_data = self.get_weather_data(self.DEFAULT_API_KEY, city)
        
        if self.central_city_data:
            self.create_weather_card(self.central_city_data)
            self.show_status(f"Weather data loaded for {city}", self.colors['success'])

    def analyze_state(self):
        """Analyze weather for multiple cities in a state"""
        state = self.state_entry.get().strip()
        if not state:
            self.show_status("Please enter a state code", self.colors['danger'])
            return
            
        self.show_status("Analyzing state weather data...", self.colors['warning'])
        cities_in_state = self.get_cities_in_state(state)
        
        if not cities_in_state:
            self.show_status(f"No cities found for state: {state}", self.colors['danger'])
            return
            
        self.state_cities_data = []
        for city in cities_in_state:
            weather = self.get_weather_data(self.DEFAULT_API_KEY, f"{city},{state},IN")
            if weather:
                self.state_cities_data.append(weather)
        
        if self.state_cities_data:
            self.create_all_carousel_plots()
            self.show_plot(0)  # Show first plot
            self.show_state_analysis_summary()
            self.show_status(f"Analysis complete for {len(self.state_cities_data)} cities", 
                           self.colors['success'])

    def create_all_carousel_plots(self):
        """Create all plots for the carousel"""
        self.current_figures = []
        self.chart_titles = []
        
        plt.style.use('default')
        df = pd.DataFrame(self.state_cities_data)
        cities = df['City']
        
        # Clean color palette
        colors = ['#007bff', '#28a745', '#ffc107', '#dc3545', '#6f42c1', 
                 '#17a2b8', '#fd7e14', '#6c757d', '#e83e8c', '#20c997']
        
        # Chart 1: Temperature Bar Chart
        fig1 = plt.Figure(figsize=(12, 8), facecolor='white')
        ax1 = fig1.add_subplot(111)
        bars = ax1.bar(cities, df['Temperature (°C)'], color=colors[:len(cities)], alpha=0.8)
        ax1.set_title('🌡️ Temperature Comparison Across Cities', 
                     fontsize=18, color='#007bff', pad=25)
        ax1.set_ylabel('Temperature (°C)', fontsize=14)
        ax1.tick_params(axis='x', rotation=45, labelsize=11)
        for tick in ax1.get_xticklabels():
            tick.set_horizontalalignment('right')
        ax1.grid(True, alpha=0.3, linestyle='--')
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                    f'{height:.1f}°', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        fig1.tight_layout()
        self.current_figures.append(fig1)
        self.chart_titles.append("Temperature Comparison")
        
        # Chart 2: Humidity Line Chart
        fig2 = plt.Figure(figsize=(12, 8), facecolor='white')
        ax2 = fig2.add_subplot(111)
        line = ax2.plot(cities, df['Humidity (%)'], marker='o', linewidth=4, 
                       markersize=10, color='#28a745', alpha=0.8)
        ax2.fill_between(cities, df['Humidity (%)'], alpha=0.3, color='#28a745')
        ax2.set_title('💧 Humidity Trends Across Cities', 
                     fontsize=18, color='#007bff', pad=25)
        ax2.set_ylabel('Humidity (%)', fontsize=14)
        ax2.tick_params(axis='x', rotation=45, labelsize=11)
        for tick in ax2.get_xticklabels():
            tick.set_horizontalalignment('right')
        ax2.grid(True, alpha=0.3, linestyle='--')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        
        # Add value labels on points
        for i, (city, humidity) in enumerate(zip(cities, df['Humidity (%)'])):
            ax2.annotate(f'{humidity:.1f}%', (i, humidity), 
                        textcoords="offset points", xytext=(0,15), ha='center',
                        fontsize=10, fontweight='bold')
        
        fig2.tight_layout()
        self.current_figures.append(fig2)
        self.chart_titles.append("Humidity Trends")
        
        # Chart 3: Wind Speed Pie Chart
        fig3 = plt.Figure(figsize=(12, 8), facecolor='white')
        ax3 = fig3.add_subplot(111)
        wedges, texts, autotexts = ax3.pie(df['Wind Speed (m/s)'], labels=cities, 
                                          autopct='%1.1f%%', colors=colors[:len(cities)],
                                          startangle=90, textprops={'fontsize': 11})
        ax3.set_title('💨 Wind Speed Distribution', 
                     fontsize=18, color='#007bff', pad=25)
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        self.current_figures.append(fig3)
        self.chart_titles.append("Wind Speed Distribution")
        
        # Chart 4: Weather Conditions Pie Chart
        conditions = df['Weather Condition'].value_counts()
        fig4 = plt.Figure(figsize=(12, 8), facecolor='white')
        ax4 = fig4.add_subplot(111)
        wedges2, texts2, autotexts2 = ax4.pie(conditions.values, labels=conditions.index, 
                                             autopct='%1.1f%%', colors=colors[:len(conditions)],
                                             startangle=90, textprops={'fontsize': 11})
        ax4.set_title('🌤️ Weather Conditions Distribution', 
                     fontsize=18, color='#007bff', pad=25)
        
        for autotext in autotexts2:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        self.current_figures.append(fig4)
        self.chart_titles.append("Weather Conditions")
        
        # Update carousel controls
        self.update_carousel_controls()

    def show_plot(self, index):
        """Display specific plot from carousel"""
        if not self.current_figures or index < 0 or index >= len(self.current_figures):
            return
        
        # Clear existing plot
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        
        # Display new plot
        fig = self.current_figures[index]
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.current_canvas = canvas
        self.current_index = index
        self.update_carousel_indicator()

    def show_next_plot(self):
        """Show next plot in carousel"""
        if self.current_figures:
            next_index = (self.current_index + 1) % len(self.current_figures)
            self.show_plot(next_index)

    def show_prev_plot(self):
        """Show previous plot in carousel"""
        if self.current_figures:
            prev_index = (self.current_index - 1) % len(self.current_figures)
            self.show_plot(prev_index)

    def update_carousel_controls(self):
        """Update carousel control visibility and state"""
        if self.current_figures:
            self.prev_btn.config(state='normal')
            self.next_btn.config(state='normal')
        else:
            self.prev_btn.config(state='disabled')
            self.next_btn.config(state='disabled')

    def update_carousel_indicator(self):
        """Update the carousel position indicator"""
        if self.current_figures:
            current_title = self.chart_titles[self.current_index]
            indicator_text = f"{current_title} ({self.current_index + 1}/{len(self.current_figures)})"
            self.chart_indicator.config(text=indicator_text, fg=self.colors['primary'])
        else:
            self.chart_indicator.config(text="No charts available", fg=self.colors['text_muted'])

    def show_state_analysis_summary(self):
        """Show comprehensive state weather analysis summary"""
        df = pd.DataFrame(self.state_cities_data)
        
        # Clear existing content
        for widget in self.weather_details_frame.winfo_children():
            widget.destroy()
            
        # Summary container
        summary_container = tk.Frame(self.weather_details_frame, bg=self.colors['bg_card'])
        summary_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(summary_container, 
                             text="📊 State Weather Analysis Summary", 
                             font=('Segoe UI', 20, 'bold'),
                             fg=self.colors['text_dark'], 
                             bg=self.colors['bg_card'])
        title_label.pack(pady=(0, 20))
        
        # Get top cities
        hottest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=True)
        coldest = self.get_top_cities(df, 'Temperature (°C)', n=3, hottest=False)
        
        # Temperature rankings
        temp_section = tk.Frame(summary_container, bg=self.colors['bg_accent'])
        temp_section.pack(fill=tk.X, pady=(0, 15), padx=5)
        
        tk.Label(temp_section, text="🌡️ Temperature Rankings", 
                font=('Segoe UI', 16, 'bold'),
                fg=self.colors['text_dark'], 
                bg=self.colors['bg_accent']).pack(pady=12)
        
        rankings_frame = tk.Frame(temp_section, bg=self.colors['bg_accent'])
        rankings_frame.pack(pady=(0, 12))
        
        tk.Label(rankings_frame, text=f"🔥 Warmest Cities: {', '.join(hottest)}", 
                font=('Segoe UI', 13),
                fg=self.colors['text_dark'], 
                bg=self.colors['bg_accent']).pack(pady=2)
        
        tk.Label(rankings_frame, text=f"❄️ Coolest Cities: {', '.join(coldest)}", 
                font=('Segoe UI', 13),
                fg=self.colors['text_dark'], 
                bg=self.colors['bg_accent']).pack(pady=2)
        
        # Weather statistics
        stats_section = tk.Frame(summary_container, bg=self.colors['bg_card'])
        stats_section.pack(fill=tk.X, pady=10)
        
        tk.Label(stats_section, text="📈 Average Weather Conditions", 
                font=('Segoe UI', 16, 'bold'),
                fg=self.colors['primary'], 
                bg=self.colors['bg_card']).pack(pady=(0, 15))
        
        # Statistics grid
        stats_grid = tk.Frame(stats_section, bg=self.colors['bg_card'])
        stats_grid.pack()
        
        avg_temp = df['Temperature (°C)'].mean()
        avg_humidity = df['Humidity (%)'].mean()
        avg_wind = df['Wind Speed (m/s)'].mean()
        
        stats_data = [
            ("Temperature", f"{avg_temp:.1f}°C"),
            ("Humidity", f"{avg_humidity:.1f}%"),
            ("Wind Speed", f"{avg_wind:.1f} m/s")
        ]
        
        for i, (label, value) in enumerate(stats_data):
            stat_frame = tk.Frame(stats_grid, bg=self.colors['bg_card'])
            stat_frame.grid(row=0, column=i, padx=35, pady=10)
            
            tk.Label(stat_frame, text=value, 
                    font=('Segoe UI', 18, 'bold'),
                    fg=self.colors['primary'], 
                    bg=self.colors['bg_card']).pack()
            
            tk.Label(stat_frame, text=label, 
                    font=('Segoe UI', 12),
                    fg=self.colors['text_muted'], 
                    bg=self.colors['bg_card']).pack()
        
        # Navigation hint
        hint_label = tk.Label(summary_container, 
                            text="💡 Use the carousel buttons above to browse through different weather charts!",
                            font=('Segoe UI', 12, 'italic'),
                            fg=self.colors['secondary'], 
                            bg=self.colors['bg_card'])
        hint_label.pack(pady=15)

    def get_cities_in_state(self, state):
        """Get cities for Indian states"""
        state_city_map = {
            "AP": ["Visakhapatnam", "Vijayawada", "Guntur", "Tirupati", "Rajahmundry"],
            "AS": ["Guwahati", "Dibrugarh", "Silchar", "Jorhat", "Tezpur"],
            "BR": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur", "Darbhanga"],
            "CG": ["Raipur", "Bhilai", "Bilaspur", "Durg", "Korba"],
            "GA": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda"],
            "GJ": ["Ahmedabad", "Surat", "Vadodara", "Gandhinagar", "Rajkot"],
            "HR": ["Gurugram", "Faridabad", "Panipat", "Ambala", "Karnal"],
            "HP": ["Shimla", "Manali", "Dharamshala", "Solan", "Mandi"],
            "JH": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh"],
            "KA": ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru", "Belagavi"],
            "KL": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Alappuzha"],
            "MP": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"],
            "MH": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
            "OR": ["Bhubaneswar", "Cuttack", "Rourkela", "Puri", "Sambalpur"],
            "PB": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda"],
            "RJ": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner"],
            "TN": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
            "TS": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam"],
            "UP": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Meerut"],
            "WB": ["Kolkata", "Howrah", "Durgapur", "Siliguri", "Asansol"]
        }
        return state_city_map.get(state.upper(), [])

    def get_weather_data(self, api_key, location):
        """Fetch weather data from OpenWeatherMap API"""
        try:
            params = {'q': location, 'appid': api_key, 'units': 'metric'}
            response = requests.get("http://api.openweathermap.org/data/2.5/weather", 
                                  params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Get additional data
            aqi = self.get_air_quality(api_key, data['coord']['lat'], data['coord']['lon'])
            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
            
            return {
                'City': data['name'],
                'Temperature (°C)': data['main']['temp'],
                'Humidity (%)': data['main']['humidity'],
                'Wind Speed (m/s)': data['wind']['speed'],
                'Weather Condition': data['weather'][0]['main'],
                'AQI': aqi,
                'Sunrise': sunrise,
                'Sunset': sunset,
                'Alerts': 'None'
            }
        except Exception as e:
            self.show_status(f"Error fetching data for {location}: {str(e)}", self.colors['danger'])
            return None

    def get_air_quality(self, api_key, lat, lon):
        """Get air quality index"""
        try:
            params = {'lat': lat, 'lon': lon, 'appid': api_key}
            response = requests.get("http://api.openweathermap.org/data/2.5/air_pollution", 
                                  params=params, timeout=5)
            response.raise_for_status()
            return response.json()['list'][0]['main']['aqi']
        except:
            return "N/A"

    def get_top_cities(self, df, column, n=3, hottest=True):
        """Get top cities using priority queue"""
        pq = PriorityQueue(is_max=not hottest)
        for index, row in df.iterrows():
            pq.push(row[column], row['City'])
            if pq.size() > n:
                pq.pop()
        
        sorted_items = pq.get_sorted_items()
        if not hottest:
            sorted_items.reverse()
        return [city for temp, city in sorted_items]

    def show_status(self, message, color="#28a745"):
        """Show status message with auto-clear"""
        self.status_label.config(text=message, fg=color)
        self.root.after(5000, lambda: self.status_label.config(
            text="Ready to analyze weather data", fg=self.colors['success']))


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAnalysisCarouselApp(root)
    root.mainloop()
