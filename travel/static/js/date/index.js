
function formatStrDate(a) {
    switch (typeof a) {
        case "string":
            return a = a.split(/-|\//g),
            a[0] + "-" + formatNum(a[1]) + "-" + formatNum(a[2]);
        case "object":
            return a.getFullYear() + "-" + formatNum(a.getMonth() + 1) + "-" + formatNum(a.getDate())
    }
}
function NewDate(a) {
    if (a!=undefined) {
        a = a.split("-");
        var c = new Date;
        c.setUTCFullYear(a[0], a[1] - 1, a[2]);
        c.setUTCHours(0, 0, 0, 0);
        return c
    }
    else
        return a;
}
function formatNum(a) {
    return a.toString().replace(/^(\d)$/, "0$1")
}
function judgeWeeks(a) {
    switch (a) {
        case 1:
            codeW = "mon";
            break;
        case 2:
            codeW = "tue";
            break;
        case 3:
            codeW = "wed";
            break;
        case 4:
            codeW = "thu";
            break;
        case 5:
            codeW = "fir";
            break;
        case 6:
            codeW = "sat";
            break;
        case 0:
            codeW = "sun"
    }
    return codeW
}
function ChangCityStr() {
    var a = $("#cfromCity").val(),
    c = $("#ctoCity").val(),
    b = document.getElementById("fromCity").value,
    e = document.getElementById("toCity").value;
    $("#ctoCity").val(a);
    document.getElementById("fromCity").value = e;
    $("#cfromCity").val(c);
    document.getElementById("toCity").value = b
}
Date.prototype.format = function (a) {
    var c = {
        "M+": this.getMonth() + 1,
        "d+": this.getDate(),
        "h+": 0 == this.getHours() % 12 ? 12 : this.getHours() % 12,
        "H+": this.getHours(),
        "m+": this.getMinutes(),
        "s+": this.getSeconds(),
        "q+": Math.floor((this.getMonth() + 3) / 3),
        S: this.getMilliseconds()
    },
    b = {
        0: "日",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六"
    };
    /(y+)/.test(a) && (a = a.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length)));
    /(E+)/.test(a) && (a = a.replace(RegExp.$1, (1 < RegExp.$1.length ? 2 < RegExp.$1.length ? "星期" : "周" : "") + b[this.getDay() + ""]));
    for (var e in c) RegExp("(" + e + ")").test(a) && (a = a.replace(RegExp.$1, 1 == RegExp.$1.length ? c[e] : ("00" + c[e]).substr(("" + c[e]).length)));
    return a
};
Date.prototype.dateAdd = function (a, c) {
    this.setDate(this.getDate() + c);
    return this
};
Date.prototype.dateDiff = function (a, c) {
    var b = {},
    e = this.getTime(),
    d = c.getTime();
    b.y = c.getFullYear() - this.getFullYear();
    b.q = 4 * b.y + Math.floor(c.getMonth() / 4) - Math.floor(this.getMonth() / 4);
    b.m = 12 * b.y + c.getMonth() - this.getMonth();
    b.ms = c.getTime() - this.getTime();
    b.w = Math.floor((d + 3456E5) / 6048E5) - Math.floor((e + 3456E5) / 6048E5);
    b.d = Math.floor(d / 864E5) - Math.floor(e / 864E5);
    b.h = Math.floor(d / 36E5) - Math.floor(e / 36E5);
    b.n = Math.floor(d / 6E4) - Math.floor(e / 6E4);
    b.s = Math.floor(d / 1E3) - Math.floor(e / 1E3);
    return b[a]
};
function str2Date(a) {
   
    try {
        a = a.split("-"),
        a = new Date(parseInt(a[0], 10), parseInt(a[1], 10) - 1, parseInt(a[2], 10))
    } catch (c) {
        a = "",
        a = "日期转换异常！\r\njs:snHotelUtil\tfunction:str2Date\r\n" + c.name + ": " + c.message,
        alert(a),
        a = new Date
    }
    return a
}
var cachedCon = [],
currentCon;
function queryHotelListByCity(a) {
    $(".hotelCon ").find(".lodingNew ").show();
    $("#list1Show").hide();
    $("#list2Show").hide();
    $("#list3Show").hide();
    for (var c = !1,
    b = 0; b < cachedCon.length; b++) if (cachedCon[b].id == a) {
        currentCon = cachedCon[b];
        c = !0;
        break
    }
    c ? showCon(currentCon.data) : $.ajax({
        type: "post",
        url: src_www + "/hotel/ajax/getHotelListByIndex.do",
        dataType: "json",
        data: "cityId\x3d" + a + "\x26typeId\x3d1",
        cache: !0,
        success: function (b) {
            cachedCon.push({
                id: a,
                data: b
            });
            currentCon = {
                id: a,
                data: b
            };
            showCon(b)
        },
        error: function () {
            $(".hotelCon ").find(".lodingNew ").hide()
        }
    })
}

ECode.calendar({
    inputBox: "#toDate",
    count: 2,
    flag: !1,
    range: {
        mindate: $("#fromDate").val()
    },
    startdate: "yyyy-mm-dd" == $("#toDate").val() ? null : $("#toDate").val(),
    week: !0,
    callback: function () {
        "yyyy-mm-dd" != $("#toDate").val() && ($("#single_way").attr("checked", ""), $("#goback_way").attr("checked", "true"))
    }
});
ECode.calendar({
    inputBox: "#fromDate",
    count: 2,
    flag: !1,
    range: {
        mindate: $("#currentTime").val()
    },
    startdate: $("#fromDate").val(),
    week: !0,
    callback: function () {
        var a = $("#toDate").val().substring(0, 10),
        c = $("#fromDate").val().substring(0, 10);
        if ("checked" == $("#airplaneRadio").find("input:eq(1)").attr("checked")) {
            a = $("#toDate").val().substring(0, 10);
          
            if (0 >= str2Date(c).dateDiff("d", str2Date(a))) {
                var a = c.split(/-|\//g),
                b = new Date(a[0], a[1] - 1, parseInt(a[2], 10) + 1),
                a = formatStrDate(b),
                b = b.getDay();
                $("#toDate").val(a);
                $("#toDate").css({
                    background: 'url("' + src_url + "/styles/images/pic_" + judgeWeeks(b) + '.png") 106px center no-repeat'
                })
            }
            ECode.calendar({
                inputBox: "#toDate",
                imgInput: "#b2",
                count: 2,
                flag: !1,
                week: !0,
                range: {
                    mindate: c
                },
                startdate: a,
                callback: function () {
                    "yyyy-mm-dd" != $("#toDate").val() && ($("#single_way").attr("checked", ""), $("#goback_way").attr("checked", "true"))
                }
            });
            $("#toDate").trigger("click")
        } else ECode.calendar({
            inputBox: "#toDate",
            count: 2,
            flag: !1,
            range: {
                mindate: $("#fromDate").val()
            },
            startdate: "yyyy-mm-dd" == $("#toDate").val() ? null : $("#toDate").val(),
            week: !0,
            callback: function () {
                "yyyy-mm-dd" != $("#toDate").val() && ($("#single_way").attr("checked", ""), $("#goback_way").attr("checked", "true"))
            }
        })
    }
});
$(function () {
   
    // c = NewDate($("#enddate").val()).getDay(),
    b = NewDate($("#fromDate").val()).getDay();
   
    // $("#enddate").css({
    //     background: 'url("' + src_url + "/styles/images/pic_" + judgeWeeks(c) + '.png") 106px center no-repeat',
    //     color: "#000"
    // });
    $("#fromDate").css({
        background: 'url("' + src_url + "/styles/images/pic_" + judgeWeeks(b) + '.png") 106px center no-repeat',
        color: "#000"
    })
});

//var MAX_DATE = str2Date($("#currentTime").val()).dateAdd("d", 90).format("yyyy-MM-dd"),
//d01 = $("#date").val().substring(0, 10),
//d02 = str2Date(d01).dateAdd("d", 1).format("yyyy-MM-dd"),
//startDate = $("#enddate").val();
//function calendarIn() {
//    ECode.calendar({
//        inputBox: "#enddate",
//        imgInput: null,
//        count: 2,
//        flag: !1,
//        range: {
//            mindate: d02,
//            maxdate: MAX_DATE
//        },
//        week: !0,
//        startdate: startDate
//    });
//    ECode.calendar({
//        inputBox: "#date",
//        count: 2,
//        flag: !1,
//        range: {
//            mindate: $("#currentTime").val(),
//            maxdate: MAX_DATE
//        },
//        week: !0,
//        startdate: d01,
//        callback: function () {
//            var a = $("#date").val().substring(0, 10),
//            c = $("#enddate").val().substring(0, 10);
//            d02 = str2Date(a).dateAdd("d", 1).format("yyyy-MM-dd");
//            0 >= str2Date(a).dateDiff("d", str2Date(c)) && $("#enddate").val(str2Date(d02).format("yyyy-MM-dd"));
//            a = a.split(/-|\//g);
//            a = new Date(a[0], a[1] - 1, parseInt(a[2], 10) + 1);
//            formatStrDate(a);
//            a = a.getDay();
//            startDate = $("#enddate").val();
//            $("#enddate").css({
//                background: 'url("' + src_url + "/styles/images/pic_" + judgeWeeks(a) + '.png") 106px center no-repeat'
//            });
//            ECode.calendar({
//                inputBox: "#enddate",
//                count: 2,
//                flag: !1,
//                range: {
//                    mindate: d02,
//                    maxdate: MAX_DATE
//                },
//                week: !0,
//                startdate: startDate
//            });
//            $("#enddate").trigger("click")
//        }
//    })
//}




