"""
CampusSpend - Student Expense Tracker Server
Hacktoberfest Ready Project

Supports running with Flask (if installed) or automatically falls back to Python's
built-in standard library http.server, requiring zero third-party packages to run.
"""

import sys
import os
import webbrowser

PORT = 5000

def run_flask():
    from flask import Flask, render_template, jsonify, request

    base_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(base_dir, 'templates')
    
    app = Flask(__name__, template_folder=templates_dir, static_folder=base_dir)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/health')
    def health():
        return jsonify({"status": "healthy", "app": "CampusSpend"})

    print(f"=======================================================")
    print(f" CampusSpend Flask Server running at: http://localhost:{PORT}")
    print(f" Zero-Gravity Mode & Antigravity xkcd #353 Ready")
    print(f"=======================================================")
    
    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass
        
    app.run(host='0.0.0.0', port=PORT, debug=True)

def run_fallback():
    import http.server
    import socketserver

    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    Handler = http.server.SimpleHTTPRequestHandler
    
    print(f"=======================================================")
    print(f" CampusSpend Server running at: http://localhost:{PORT}")
    print(f" Serving index.html via Python http.server")
    print(f"=======================================================")
    
    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == '__main__':
    try:
        import flask
        run_flask()
    except ImportError:
        print("[Notice] Flask is not installed in this environment. Falling back to built-in http.server.")
        run_fallback()
