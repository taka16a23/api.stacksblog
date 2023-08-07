export function digitToHyphenYuubinBangou(value) {
  let v = String(value);
  if(v === "") {
    return "";
  }
  if(isNaN(v) === true) {
    throw Error("value required numeric. got(" + v + ")");
  }
  if(v.length !== 7) {
    return "";
  }
  return v.substr(0, 3) + "-" + v.substr(3);
}
