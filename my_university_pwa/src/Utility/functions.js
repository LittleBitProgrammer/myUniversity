export function capitalizeFirstLetter(string){
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

export function formatDate (input) {
  return input.split("-").reverse().join("-");
}