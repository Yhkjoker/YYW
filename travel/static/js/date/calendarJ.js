var ECode = ECode || {};
ECode.calendar = function (x) {
    function l(a) {
        return a.toString().replace(/^(\d)$/, "0$1")
    }
    function s(a) {
        switch (typeof a) {
            case "string":
                return a = a.split(/-|\//g),
                a[0] + "-" + l(a[1]) + "-" + l(a[2]);
            case "object":
                return a.getFullYear() + "-" + l(a.getMonth() + 1) + "-" + l(a.getDate())
        }
    }
    function t(a) {
        return s(a).replace(/-|\//g, "")
    }
    var g = {
        inputBox: null,
        imgInput: null,
        isSelect: !1,
        showbox: null,
        range: {
            mindate: new Date,
            maxdate: null
        },
        count: 1,
        startdate: null,
        flag: !0,
        week: !0,
        pathImg: "",
        callback: function () { },
        cur: !0
    },
    v = {
        today: "今天",
        yuandan: "元旦",
        chuxi: "除夕",
        chunjie: "春节",
        yuanxiao: "元宵节",
        qingming: "清明",
        wuyi: "劳动节",
        duanwu: "端午节",
        zhongqiu: "中秋节",
        guoqing: "国庆节"
    },
    y = {
        today: [s(new Date)],
        yuandan: "2012-01-01 2013-01-01 2014-01-01 2015-01-01 2016-01-01 2017-01-01 2018-01-01 2019-01-01 2020-01-01".split(" "),
        chuxi: "2012-01-22 2013-02-09 2014-01-30 2015-02-18 2016-02-07 2017-01-27 2018-02-15 2019-02-04 2020-01-24".split(" "),
        chunjie: "2012-01-23 2013-02-10 2014-01-31 2015-02-19 2016-02-08 2017-01-28 2018-02-16 2019-02-05 2020-01-25".split(" "),
        yuanxiao: "2012-02-06 2013-02-24 2014-2-14 2015-03-05 2016-02-22 2017-02-11 2018-03-02 2019-02-19 2020-02-8".split(" "),
        qingming: "2012-04-04 2013-04-04 2014-04-05 2015-04-05 2016-04-04 2017-04-04 2018-04-05 2019-04-05 2020-04-04".split(" "),
        wuyi: "2012-05-01 2013-05-01 2014-05-01 2015-05-01 2016-05-01 2017-05-01 2018-05-01 2019-05-01 2020-05-01".split(" "),
        duanwu: "2012-06-23 2013-06-12 2014-06-02 2015-06-20 2016-06-09 2017-05-30 2018-06-18 2019-06-07 2020-06-25".split(" "),
        zhongqiu: "2012-09-30 2013-09-19 2014-09-08 2015-09-27 2016-09-15 2017-10-04 2018-09-24 2019-09-13 2020-10-01".split(" "),
        guoqing: "2012-10-01 2013-10-01 2014-10-01 2015-10-01 2016-10-01 2017-10-01 2018-10-01 2019-10-01 2020-10-01".split(" ")
    };
    if (0 < arguments.length && "object" == typeof arguments[0]) $.extend(g, x);
    else return !1;
    var f = $(g.inputBox),
    z = $(g.imgInput),
    h = g.showbox,
    p = g.callback,
    m = g.startdate; ({
        init: function () {
            var a = this;
            f.unbind("click").bind("click",
            function (c) {
                var e;
                null == h ? "INPUT" === $(this)[0].tagName.toUpperCase() ? e = $(this).val() : e = $(this).text() : "INPUT" === $(h)[0].tagName.toUpperCase() ? e = $(h).val() : e = $(h).text();
                $(".calendar").remove();
                a.createContainer();
                a._creade();
                null !== m ? (c = m.split(/-|\//g), a.render(new Date(c[0], c[1] - 1, c[2]))) : RegExp(/^\d{4}(\-|\/)\d{2}\1\d{2}$/).test(e) ? (c = e.split(/-|\//g), a.render(new Date(c[0], c[1] - 1, c[2]))) : a.render(new Date)
            });
            z.unbind("click").bind("click",
            function (a) {
                f.click();
                a.stopPropagation()
            });
            f.unbind("focus").bind("focus",
            function (a) {
                $(this).trigger("click")
            })
        },
        _creade: function () {
            var a = [];
            this.dateWarp = $("\x3cdiv\x3e\x3c/div\x3e");
            this.dateWarp.attr("class", "calendar");
            for (i = this.count = g.count; i--;) a = a.concat(this._template);
            this.dateWarp.append($('\x3cspan class\x3d"cal-prev"\x3e\x3c/span\x3e\x3cspan class\x3d"cal-next"\x3e\x3c/span\x3e' + a.join("")));
            this.container.append(this.dateWarp);
            window.ActiveXObject && !window.XMLHttpRequest && this.dateWarp.append($(this.createIframe()))
        },
        render: function (a) {
            var c = this.container.find(".cal-container"),
            e,
            k,
            f;
            e = a.getFullYear();
            a = a.getMonth() + 1;
            this.year = e;
            this.month = a;
            k = 0;
            for (f = c.length; k < f; k++) e += 12 < a + (k ? 1 : 0) ? 1 : 0,
            a = (a + (k ? 1 : 0)) % 12 || 12,
            this.drawDate(c.eq(k), {
                year: e,
                month: a
            });
            g.isSelect ? this.selectChange() : this.btnEvent()
        },
        _template: '\x3cdiv class\x3d"cal-container"\x3e;\x3cdl\x3e;\x3cdt class\x3d"title-date"\x3e;\x3c/dt\x3e;\x3cdt class\x3d"first"\x3e\x3cstrong\x3e日\x3c/strong\x3e\x3c/dt\x3e;\x3cdt\x3e一\x3c/dt\x3e;\x3cdt\x3e二\x3c/dt\x3e;\x3cdt\x3e三\x3c/dt\x3e;\x3cdt\x3e四\x3c/dt\x3e;\x3cdt\x3e五\x3c/dt\x3e;\x3cdt class\x3d"last"\x3e\x3cstrong\x3e六\x3c/strong\x3e\x3c/dt\x3e;\x3cdd\x3e\x3c/dd\x3e;\x3c/dl\x3e;\x3c/div\x3e'.split(";"),
        createContainer: function () {
            var a = $("#" + f.attr("id") + "-date");
            a && a.remove();
            var a = f.position(),
            c = this.container = $("\x3cdiv\x3e\x3c/div\x3e");
            c.attr("id", f.attr("id") + "-date");
            c.css({
                position: "absolute",
                zIndex: 999,
                width: 456,
                left: a.left,
                top: f.outerHeight()
            });
            c.bind("click",
            function (a) {
                a.stopPropagation()
            });
            f.parent().append(c)
        },
        drawDate: function (a, c) {
            var e, k, h, q, b, r, d, n = [],
            u,
            p = document.createDocumentFragment();
            h = c.year;
            q = c.month;
            e = this.dateWarp;
            this.titleDate = k = a.find(".title-date");
            if (g.isSelect) {
                b = [];
                b.push("\x3cselect\x3e");
                for (d = 2020; 1970 < d; d--) d != this.year ? b.push('\x3coption value\x3d"' + d + '"\x3e' + d + "\x3c/option\x3e ") : b.push('\x3coption value\x3d"' + d + '" selected\x3e' + d + "\x3c/option\x3e ");
                b.push("\x3c/select\x3e");
                b.push(" \x3cem\x3e年\x3c/em\x3e ");
                b.push("\x3cselect\x3e");
                for (d = 1; 13 > d; d++) d != this.month ? b.push('\x3coption value \x3d"' + d + '"\x3e' + d + "\x3c/option\x3e") : b.push('\x3coption value \x3d"' + d + '" selected\x3e' + d + "\x3c/option\x3e");
                b.push("\x3c/select\x3e");
                b.push(" \x3cem\x3e月\x3c/em\x3e ");
                k.html($(b.join("")));
                $(".cal-prev").remove();
                $(".cal-next").remove();
                this.dateWarp.css("padding", "0 0 15px")
            } else k.html(h + "年" + q + "月");
            this.dd = k = a.find("dd");
            b = (new Date(h, q, 0)).getDate();
            r = (new Date(h, q - 1, 1)).getDay();
            for (d = 0; d < r; d++) n.push(0);
            for (d = 1; d <= b; d++) n.push(d);
            for (; n.length;) for (d = 0; d < n.length; d++) if (n.length) {
                b = document.createElement("a"); (r = n.shift()) ? (b.href = "javascript:;", b.innerHTML = r, b["data-date"] = h + "-" + l(q) + "-" + l(r), b["data-date"] == m && ("" == b.className ? b.className = "startdate" : b.className += "startdate"), u = t(b["data-date"])) : (b.className = "disabled", b.innerHTML = "\x26nbsp;");
                g.range.mindate && u < t(s(g.range.mindate)) && (b.className = "disabled");
                g.range.maxdate && u > t(s(g.range.maxdate)) && (b.className = "disabled");
                g.flag && null !== m && u > t(m) && "disabled" !== b.className && (b.className = "hover");
                for (var w in v) "disabled" != b.className && RegExp(b["data-date"]).test(y[w].join()) && ("" == b.className ? b.className = "holiday" : b.className += " holiday", b.innerHTML = v[w]);
                p.appendChild(b)
            }
            k.html($(p));
            this.removeDate();
            f.parent().css("z-index", "9999");
            this.container.html(e);
            this.linkOn();
            this.outClick()
        },
        createIframe: function () {
            var a = document.createElement("iframe");
            a.src = "about:blank";
            a.style.position = "absolute";
            a.style.zIndex = -1;
            a.style.left = "-1px";
            a.style.top = 0;
            a.style.border = 0;
            a.style.background = "#000";
            a.style.filter = "alpha(opacity\x3d 0 )";
            a.style.width = this.container.width() + "px";
            a.style.height = this.container.height() + "px";
            return a
        },
        removeDate: function () {
            this.container.find(".calendar") && this.container.empty();
            f.parent().css("z-index", "")
        },
        btnEvent: function () {
            var a = this.container.find(".cal-prev"),
            c = this.container.find(".cal-next"),
            e = this;
            a.click(function () {
                e.render(new Date(e.year, e.month - 2, 1))
            });
            c.click(function () {
                e.render(new Date(e.year, e.month, 1))
            })
        },
        selectChange: function () {
            var a, c, e = this;
            a = this.container.find(".cal-container").find("select").eq(0);
            c = this.container.find(".cal-container").find("select").eq(1);
            a.change(function () {
                var f = a.val(),
                g = c.val();
                e.render(new Date(f, g - 1))
            });
            c.change(function () {
                var f = a.val(),
                g = c.val();
                e.render(new Date(f, g - 1))
            })
        },
        linkOn: function () {
            this.dateWarp.find("a").not(".disabled");
            var a = this;
            this.dateWarp.delegate("a", "click",
            function (c) {
                if (!$(this).hasClass("disabled")) {
                    c.stopPropagation();
                    c = $(this)[0]["data-date"].split(/-|\//g);
                    switch ((new Date(c[0], c[1] - 1, c[2])).getDay()) {
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
                    null == h ? ("INPUT" === f[0].tagName.toUpperCase() ? f.val($(this)[0]["data-date"]) : f.text($(this)[0]["data-date"]), g.week && f.css({
                        background: 'url("' + src_url + "/styles/images/pic_" + codeW + '.png") 106px center no-repeat ',
                        color: "#000"
                    })) : ("INPUT" === $(h)[0].tagName.toUpperCase() ? $(h).val($(this)[0]["data-date"]) : $(h).text($(this)[0]["data-date"]), g.week && $(h).css({
                        background: 'url("' + src_url + "/styles/images/pic_" + codeW + '.png") 106px center no-repeat ',
                        color: "#000"
                    })); !0 == g.cur && (m = $(this)[0]["data-date"]);
                    $(this).closest("tr").siblings("tr").find(".credential").focus();
                    a.removeDate();
                    p && p()
                }
            })
        },
        outClick: function () {
            var a = this;
            $(document).bind("click",
            function (c) {
                if (c.target.id == f[0].id) return !1;
                a.removeDate()
            })
        }
    }).init()
};
