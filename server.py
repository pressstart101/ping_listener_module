@app.route('/api/ping.json')
def ping():


    time.sleep(3)
    p = ping_init.get_pings()

    return jsonify(p)
