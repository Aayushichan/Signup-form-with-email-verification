// Disable screenshot functionality
document.addEventListener("keydown", function(e) {
    // Pressing "PrtScn" key
    if (e.key === "PrintScreen") {
        e.preventDefault();
        alert("Sorry, taking screenshots is not allowed on this website.");
    }
    // Pressing "Ctrl + Shift + I" key combination
    if (e.ctrlKey && e.shiftKey && e.key === "I") {
        e.preventDefault();
        alert("Sorry, using developer tools is not allowed on this website.");
    }
});
