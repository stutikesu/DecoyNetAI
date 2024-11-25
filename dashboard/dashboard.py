from flask import Flask, render_template
import random  # Simulating trap data for now

app = Flask(__name__)

@app.route('/')
def dashboard():
    
    active_traps = fetch_active_traps()  
    
    
    return render_template('dashboard.html', traps=active_traps)

def fetch_active_traps():
    
    return random.randint(5, 20)

if __name__ == '__main__':
    app.run(debug=True)
