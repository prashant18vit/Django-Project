window.onload = initall;

var saveansBtn;
function initall() {
  saveansBtn = document.getElementById("save_ans");
  saveques = document.getElementById("question_a").textContent;
  saveansBtn.onclick = saveans;
  var no = saveques;
  console.log(no);
}

function saveans() {
  var ans = $("input:radio[name=name]:checked").val();
  alert("ans is submitted");
  var req = new XMLHttpRequest();

  var URL = "/saveans?ans=" + ans;
  req.open("GET", URL);
  req.send();
}
