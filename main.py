from pyscript import document, display

def general_weighted_average(e):
    first_name = document.getElementById("firstname").value
    last_name = document.getElementById("lastname").value

    science = float(document.getElementById("science").value)
    math = float(document.getElementById("math").value)
    english = float(document.getElementById("english").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)
    pe = float(document.getElementById("pe").value)

    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]

    units_subject = (5, 3, 2, 1)

    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

    summary = f"""
    {subjects[0]}: {science:.0f}
    {subjects[1]}: {math:.0f}
    {subjects[2]}: {english:.0f}
    {subjects[3]}: {filipino:.0f}
    {subjects[4]}: {ict:.0f}
    {subjects[5]}: {pe:.0f}
    """

    display(f'Name: {first_name} {last_name}', target="form-group")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
    
    # def clear_info(e):
    #     document.getElementById("firstname").value = ""
    #     document.getElementById("lastname").value = ""
    #     document.getElementById("science").value = ""
    #     document.getElementById("math").value = ""
    #     document.getElementById("english").value = ""
    #     document.getElementById("filipino").value = ""
    #     document.getElementById("ict").value = ""
    #     document.getElementById("pe").value = ""
    #     document.getElementById("submit_order").innerHTML = ""
    #     document.getElementById("summary").innerHTML = ""
    #     document.getElementById("output").innerHTML = ""

    #     result = document.getElementById("output")
    #     result.innerHTML = ""
        
