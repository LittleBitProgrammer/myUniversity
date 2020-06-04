export function capitalizeFirstLetter(string){
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

export function formatDate (input) {
  return input.split("-").reverse().join("-");
}

export function takeDate(inpuTime) {
    return inpuTime.slice(0,10);
}

export function takeTime(inpuTime) {
    return inpuTime.slice(10);
}

export function trimMessage(message) {
    if(message.length > 60)
        return message.slice(0,55)+" ...";
    return message.slice(0,55);
}