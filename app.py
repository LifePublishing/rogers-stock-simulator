from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result1 = result2 = result3 = None

    if request.method == "POST":
        try:
            investment = float(request.form["investment"])
            core1 = float(request.form["core1"])
            core2 = float(request.form["core2"])
            satellite = float(request.form["satellite"])

            # 固定の比率
            core1_weight = 0.4
            core2_weight = 0.4
            satellite_weight = 0.2

            # 推奨株数を計算
            result1 = int(investment * core1_weight / core1)
            result2 = int(investment * core2_weight / core2)
            result3 = int(investment * satellite_weight / satellite)

        except (ValueError, ZeroDivisionError):
            result1 = result2 = result3 = "エラー"

    return render_template(
        "index.html",
        result1=result1,
        result2=result2,
        result3=result3
    )

if __name__ == '__main__':
    app.run(debug=True)
