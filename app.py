from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# win code
def calculate(data):
    total = 0
    mess = ""

    data = data.splitlines()
    clean_data = [i.split(':')[-1].strip() if ":" in i else i.strip() for i in data]

    for i in clean_data:
        spli = i.split('-')

        if len(spli) < 3:
            if len(spli[0]) == 1:  # single
                ans = int(spli[1]) * 9.5
                total += ans
                mess += f'{i} = {ans}\n'
            elif len(spli[0]) == 2:  # jodi
                ans = int(spli[1]) * 95
                total += ans
                mess += f'{i} = {ans}\n'
            elif len(spli[0]) == 3:  # pana
                if len(set(str(spli[0]))) == 3:  # SP
                    ans = int(spli[1]) * 150
                elif len(set(str(spli[0]))) == 2:  # DP
                    ans = int(spli[1]) * 300
                elif len(set(str(spli[0]))) == 1:  # TP
                    ans = int(spli[1]) * 600
                else:
                    mess += 'Error\n'
                    continue
                total += ans
                mess += f'{i} = {ans}\n'
            else:
                mess += 'Error\n'
        else:
            if spli[0].lower() == "sp":
                ans = int(spli[2]) * 150
            elif spli[0].lower() == "dp":
                ans = int(spli[2]) * 300
            elif spli[0].lower() == "tp":
                ans = int(spli[2]) * 600
            else:
                mess += 'Error\n'
                continue
            total += ans
            mess += f'{i} = {ans}\n'

    return mess, total



@app.route('/')
def home():
    return render_template('index.html')

# Win cal
@app.route("/win", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_data = request.form["data"]
        return redirect(url_for("result", data=user_data))
    return render_template("win_index.html")

@app.route("/win/result")
def result():
    data = request.args.get("data", "")
    mess, total = calculate(data)
    return render_template("win_result.html", mess=mess.split("\n"), total=total)


# Message gen






@app.route("/message", methods=["GET", "POST"])
def message():
    mess = ""
    if request.method == "POST":
        nums = list(request.form["nums"])
        amount = int(request.form["amount"])
        market = request.form["market"]

        ank = amount * 16
        dp = int(amount * 0.5)

        ank_str = ""
        dp_str = ""

        for i in nums:
            ank_str += f"{i}={ank}\n"
            dp_str += f"{i}={dp}\n"

        mess = (f"{market}\n"
                f"{ank_str}"
                f"Total {ank * len(nums)}\n\n"
                f"{market}\n"
                f"DP\n"
                f"{dp_str}"
                f"Total {int(len(nums) * amount * 4.5)}")


    return render_template("dp_index.html", message=mess)



if __name__ == '__main__':
    app.run(debug=True)


