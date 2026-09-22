// Stephens Croquet Club, direction C — small progressive enhancements.
// Nothing here hides content: every element it touches is already visible
// and readable in the static HTML; this only refines the text in place.

(function () {
  "use strict";

  var DAY_INDEX = { Sunday: 0, Monday: 1, Tuesday: 2, Wednesday: 3, Thursday: 4, Friday: 5, Saturday: 6 };

  function parseTime(t) {
    var m = /(\d+)(?::(\d+))?\s*([ap]m)/i.exec(t);
    if (!m) return null;
    var h = parseInt(m[1], 10);
    var min = m[2] ? parseInt(m[2], 10) : 0;
    if (/pm/i.test(m[3]) && h !== 12) h += 12;
    if (/am/i.test(m[3]) && h === 12) h = 0;
    return { h: h, min: min };
  }

  function inSeason(note, now) {
    if (!note) return true;
    var month = now.getMonth() + 1; // 1-12
    if (/September to April/i.test(note)) return month >= 9 || month <= 4;
    if (/May to August/i.test(note)) return month >= 5 && month <= 8;
    return true;
  }

  function nextPlay(schedule, now) {
    var best = null;
    schedule.forEach(function (row) {
      if (!inSeason(row.note, now)) return;
      var time = parseTime(row.time);
      if (!time) return;
      var dayIdx = DAY_INDEX[row.day];
      for (var add = 0; add < 8; add++) {
        var candidate = new Date(now);
        candidate.setHours(time.h, time.min, 0, 0);
        var diffDays = (dayIdx - now.getDay() + 7) % 7;
        candidate.setDate(now.getDate() + diffDays + (add === 0 ? 0 : 7 * Math.floor(add / 1)));
        if (add > 0) continue;
        if (candidate < now) candidate.setDate(candidate.getDate() + 7);
        if (!best || candidate < best.when) best = { when: candidate, code: row.code, day: row.day, time: row.time };
        break;
      }
    });
    return best;
  }

  function pad(n) { return n < 10 ? "0" + n : String(n); }

  function renderCountdown() {
    var tile = document.querySelector(".tile--countdown");
    if (!tile) return;
    var data = tile.getAttribute("data-schedule");
    if (!data) return;
    var schedule;
    try { schedule = JSON.parse(data); } catch (e) { return; }
    var valueEl = document.getElementById("next-play-value");
    var subEl = document.getElementById("next-play-sub");
    if (!valueEl || !subEl) return;

    function tick() {
      var now = new Date();
      var best = nextPlay(schedule, now);
      if (!best) return;
      valueEl.textContent = best.code + " " + best.day + ", " + best.time;
      var diffMs = best.when - now;
      if (diffMs <= 0) { subEl.textContent = "Under way now"; return; }
      var totalSec = Math.floor(diffMs / 1000);
      var days = Math.floor(totalSec / 86400);
      if (days >= 1) {
        subEl.textContent = "Next session in " + days + (days === 1 ? " day" : " days");
        return;
      }
      var hrs = Math.floor(totalSec / 3600);
      var mins = Math.floor((totalSec % 3600) / 60);
      var secs = totalSec % 60;
      subEl.textContent = "Next session in " + pad(hrs) + ":" + pad(mins) + ":" + pad(secs);
    }

    tick();
    // Only reached once per second at most; refines already-visible text,
    // never creates content that wasn't there with JS off.
    setInterval(tick, 1000);
  }

  function animateStats() {
    document.querySelectorAll(".tile__stat-number[data-target]").forEach(function (el) {
      var target = parseInt(el.getAttribute("data-target"), 10);
      if (isNaN(target)) return;
      var start = target > 100 ? target - 40 : 0;
      var current = start;
      var step = Math.max(1, Math.round((target - start) / 20));
      var timer = setInterval(function () {
        current += step;
        if (current >= target) { current = target; clearInterval(timer); }
        el.textContent = current;
      }, 30);
    });
  }

  function wireLightboxEscape() {
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      var open = document.querySelector(".lightbox:target");
      if (open) window.location.hash = "";
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderCountdown();
    animateStats();
    wireLightboxEscape();
  });
})();
