function skillMember() {
  var skill = document.getElementById("skill").value;
  var member = document.getElementById("member").value;
  var url = "members.php?skill=" + skill + "&member=" + member;

  // Call the function to load the data
  load(url);
}
