function helloNalios() {
    // Compute each character from ASCII codes
    const codes = [
        72,                       // H
        101,                      // e
        108, 108,                 // l, l
        111,                      // o
        44,                       // ,
        32,                       // space
        78,                       // N
        97, 108, 105, 111, 115,  // a, l, i, o, s
        32,                       // space
        33                        // exclamation mark
    ];

    console.log(String.fromCharCode(...codes));
}

// Never done testing on JS, for the sake of simplicity i tested the call on the browser's console
helloNalios();