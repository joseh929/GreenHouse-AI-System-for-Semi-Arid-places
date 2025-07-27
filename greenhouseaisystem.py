import random
import time

def simulate_greenhouse_system():
    """Smart Greenhouse Decision Support System for Kenyan Farmers"""
    
    print("\n--- Welcome to Smart Greenhouse Decision Support System ---")
    print("--- Designed for Semi-Arid Agriculture By Joseph Ndirangu---\n")
    
    # Initial system status
    irrigation_status = "OFF"
    shading_status = "OFF" 
    consecutive_alerts = 0
    critical_flag = False
    soil_moisture_history = []
    print("-- Initial System Status --")
    print(f"Irrigation status is: {irrigation_status}")
    print(f"Shading status is: {shading_status}\n")
    
    # Simulate 10 time intervals (hours) for a real time environmental input
    for interval in range(1, 11):
        print(f"---HOUR{interval} ---")
        
        # random sensor data (realistic ranges for Kenya)
        temperature = random.uniform(20, 42)  # °C
        humidity = random.uniform(15, 80)     # %
        light_intensity = random.uniform(0, 1400)  # lux
        soil_moisture = random.uniform(15, 75)     # %
        co2_level = random.uniform(400, 1400)      # ppm
        
        # Store soil moisture for trend analysis
        soil_moisture_history.append(soil_moisture)
        
        # Display the current  readings of given inputs received above
        print("-- Sensor Readings --")
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Humidity: {humidity:.1f}%")
        print(f"Light Intensity: {light_intensity:.1f} lux")
        print(f"Soil Moisture: {soil_moisture:.1f}%")
        print(f"CO₂ Level: {co2_level:.1f} ppm")
        
        # FUZZY AI WATERING CONTROL
        if soil_moisture < 35 and (humidity < 40 or temperature > 30):
            irrigation_status = "FULL WATERING"
            reason = f"Low soil moisture ({soil_moisture:.1f}%) with stress conditions"
        elif 35 <= soil_moisture <= 50 and temperature > 35:
            irrigation_status = "LIGHT WATERING"
            reason = f"Moderate moisture but high temperature ({temperature:.1f}°C)"
        elif soil_moisture > 70:
            irrigation_status = "SKIP WATERING"
            reason = f"High soil moisture ({soil_moisture:.1f}%)"
        else:
            irrigation_status = "NO WATERING"
            reason = f"Adequate soil moisture ({soil_moisture:.1f}%)"
        
        # SHADING CONTROL using the if else LOGIC
        # Categorize light intensity
        if light_intensity < 300:
            light_category = "VERY LOW"
        elif 300 <= light_intensity <= 800:
            light_category = "MODERATE"
        elif 800 < light_intensity <= 1000:
            light_category = "HIGH"
        else:
            light_category = "VERY HIGH"
        
        # Applying switch-case logic for shading
        match light_category:
            case "VERY LOW":
                shading_status = "OPEN SHADES"
                shade_reason = f"Very low light ({light_intensity:.0f} lux) - maximize sunlight"
            case "MODERATE":
                shading_status = "NO ACTION"
                shade_reason = f"Moderate light ({light_intensity:.0f} lux) - optimal conditions"
            case "HIGH":
                shading_status = "CLOSE PARTIALLY"
                shade_reason = f"High light ({light_intensity:.0f} lux) - partial shading needed"
            case "VERY HIGH":
                shading_status = "CLOSE FULLY"
                shade_reason = f"Very high light ({light_intensity:.0f} lux) - full protection needed"
        
        # message and action to take
        print("\n-- AI Decisions --")
        print(f"Irrigation status is : {irrigation_status}")
        print(f"Reason: {reason}")
        print(f"Shading status is: {shading_status}")
        print(f"Reason: {shade_reason}")
        
        #RISK ALERT SYSTEM from the output of the sensor
        alerts = []
        alert_count = 0
        
        # Checking risk conditions
        if temperature > 36:
            alert_count += 1
            alerts.append(f"High temperature: {temperature:.1f}°C")
        
        if humidity < 25:
            alert_count += 1
            alerts.append(f"Low humidity: {humidity:.1f}%")
        
        if co2_level > 1200:
            alert_count += 1
            alerts.append(f"High CO₂: {co2_level:.0f} ppm")
        
        if soil_moisture < 30:
            alert_count += 1
            alerts.append(f"Low soil moisture: {soil_moisture:.1f}%")
        
        if light_intensity > 1100:
            alert_count += 1
            alerts.append(f"Excessive light: {light_intensity:.0f} lux")
        
        # Risk checking
        if alert_count >= 3:
            consecutive_alerts += 1
            print(f"\n  RISK ALERT TRIGGERED! ({alert_count}/5 conditions met)")
            print("Critical conditions detected:")
            for alert in alerts:
                print(f"  • {alert}")
            
            # Check for critical flag (more than 2 consecutive alerts)
            if consecutive_alerts > 2:
                critical_flag = True
                print(" CRITICAL RISK FLAG ACTIVATED!")
                print("   Immediate farmer intervention required!")
        else:
            consecutive_alerts = 0
            print(f"\n System Normal - {alert_count}/5 risk conditions detected")
        
       
        if interval >= 3 and interval % 3 == 0:
            recent_moisture = soil_moisture_history[-3:]
            avg_moisture = sum(recent_moisture) / len(recent_moisture)
            trend = recent_moisture[-1] - recent_moisture[0]
            
            print(f"\n AI Trend Analysis:")
            if trend < -5:
                print(f"    Declining moisture (avg: {avg_moisture:.1f}%) - increase watering frequency")
            elif trend > 5:
                print(f"    Rising moisture (avg: {avg_moisture:.1f}%) - reduce watering")
            else:
                print(f"   Stable moisture (avg: {avg_moisture:.1f}%) - maintain schedule")
        
        print(f"\n{'='*50}")
        time.sleep(0.5)  # Simulate real-time delay
    
    # FINAL SUMMARY
    print("\n SIMULATION COMPLETE!")
    print("="*50)
    total_watering = sum(1 for i in range(len(soil_moisture_history)) if soil_moisture_history[i] < 40)
    avg_moisture = sum(soil_moisture_history) / len(soil_moisture_history)
    
    print(f"Average soil moisture: {avg_moisture:.1f}%")
    print(f"Intervals requiring water: {total_watering}/10")
    print(f"Critical flag status: {'ACTIVE' if critical_flag else 'NORMAL'}")

# Main execution
if __name__ == "__main__":
    simulate_greenhouse_system()