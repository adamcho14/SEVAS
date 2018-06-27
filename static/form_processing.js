/**
 * Created by Adam on 09/04/2018.
 */

//vote encryption, sending login without giving the user possibility to manipulate with it
function countRadios(radios) {
    var num = 0;
   for (i = 0; i < radios.length; i++) {
       if ((radios[i].value == "1") && (radios[i].checked)) {
           num++;
       }
   }
   return num;
}

function validateForm(form, max) {
    if (countRadios(form) > max) {
        alert('Zvolili ste veľa kandidátov. Môžete najviac ' + max + '.');
        return false;
    }
    return true;
}

function encryptVote(vote) {
    const pubkey =
  ['-----BEGIN PGP PUBLIC KEY BLOCK-----',
  'Version: Keybase OpenPGP v1.0.0',
  '',
  'mI0EUmEvTgEEANyWtQQMOybQ9JltDqmaX0WnNPJeLILIM36sw6zL0nfTQ5zXSS3+',
  'fIF6P29lJFxpblWk02PSID5zX/DYU9/zjM2xPO8Oa4xo0cVTOTLj++Ri5mtr//f5',
  'GLsIXxFrBJhD/ghFsL3Op0GXOeLJ9A5bsOn8th7x6JucNKuaRB6bQbSPABEBAAG0',
  'JFRlc3QgTWNUZXN0aW5ndG9uIDx0ZXN0QGV4YW1wbGUuY29tPoi5BBMBAgAjBQJS',
  'YS9OAhsvBwsJCAcDAgEGFQgCCQoLBBYCAwECHgECF4AACgkQSmNhOk1uQJQwDAP6',
  'AgrTyqkRlJVqz2pb46TfbDM2TDF7o9CBnBzIGoxBhlRwpqALz7z2kxBDmwpQa+ki',
  'Bq3jZN/UosY9y8bhwMAlnrDY9jP1gdCo+H0sD48CdXybblNwaYpwqC8VSpDdTndf',
  '9j2wE/weihGp/DAdy/2kyBCaiOY1sjhUfJ1GogF49rC4jQRSYS9OAQQA6R/PtBFa',
  'JaT4jq10yqASk4sqwVMsc6HcifM5lSdxzExFP74naUMMyEsKHP53QxTF0Grqusag',
  'Qg/ZtgT0CN1HUM152y7ACOdp1giKjpMzOTQClqCoclyvWOFB+L/SwGEIJf7LSCEr',
  'woBuJifJc8xAVr0XX0JthoW+uP91eTQ3XpsAEQEAAYkBPQQYAQIACQUCUmEvTgIb',
  'LgCoCRBKY2E6TW5AlJ0gBBkBAgAGBQJSYS9OAAoJEOCE90RsICyXuqIEANmmiRCA',
  'SF7YK7PvFkieJNwzeK0V3F2lGX+uu6Y3Q/Zxdtwc4xR+me/CSBmsURyXTO29OWhP',
  'GLszPH9zSJU9BdDi6v0yNprmFPX/1Ng0Abn/sCkwetvjxC1YIvTLFwtUL/7v6NS2',
  'bZpsUxRTg9+cSrMWWSNjiY9qUKajm1tuzPDZXAUEAMNmAN3xXN/Kjyvj2OK2ck0X',
  'W748sl/tc3qiKPMJ+0AkMF7Pjhmh9nxqE9+QCEl7qinFqqBLjuzgUhBU4QlwX1GD',
  'AtNTq6ihLMD5v1d82ZC7tNatdlDMGWnIdvEMCv2GZcuIqDQ9rXWs49e7tq1NncLY',
  'hz3tYjKhoFTKEIq3y3Pp',
  '=h/aX',
  '-----END PGP PUBLIC KEY BLOCK-----'].join('\n');

    var x = document.forms["voting"];

    options = {
        data: vote,
        publicKeys: openpgp.key.readArmored(pubkey).keys
    };

    openpgp.encrypt(options).then(function (ciphertext) {
        x["vote"].value = ciphertext.data;
        document.getElementById("display_vote").innerHTML = ciphertext.data;
        alert("Hlas bol úspešne vytvorený.");
    });
}


function createVote(radios) {
    var vote = "";
    for (i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            vote += "<";
            vote += radios[i].name.toString();
            vote += "#";
            vote += radios[i].value.toString();
            vote += ">";
        }
    }
    return vote;
}

function wipeOut(radios) {
    for (i = 0; i < radios.length; i++) {
        radios[i].value = "";
    }
}

async function processForm(max) {
    var x = document.forms["voting"];

    if (!validateForm(x, max)) {
        return false;
    }
    my_vote = createVote(x);
    wipeOut(x); //erases form data
    x["submit"].type = "submit";
    x["submit"].value = "Pošli hlas";
    await encryptVote(my_vote);
    return true;
}
