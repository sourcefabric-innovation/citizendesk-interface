// > hide('the rest should stay secret')
// '************************ret'
function hide(s, n) {
  if(typeof n == 'undefined') {
    n = 3;
  }
  if(typeof s == 'undefined') {
    return s;
  }
  var separator = s.length - n,
      result = '';
  for(var i=0; i<separator; i++) {
    result += '*';
  }
  return result + s.slice(separator);
}

module.exports = {
  hide: hide
}