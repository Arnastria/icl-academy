$('#btn-submit-daftar').click(function () {
    console.log("Aye!")
    var name = $('#input-name').val();
    var tempat_lahir = $('#input-tempat-lahir').val();
    var tanggal_lahir = $('#input-tanggal-lahir').val();
    var gender = $('#input-gender').val();
    var pekerjaan = $('#input-pekerjaan').val();
    var alamat = $('#input-alamat').val();
    var hp = $('#input-hp').val();
    var pendidikan = $('#input-pendidikan').val();

    var data = {}
    data['name'] = name;
    data['tempat_lahir'] = tempat_lahir;
    data['tanggal_lahir'] = tanggal_lahir;
    data['gender'] = gender;
    data['pekerjaan'] = pekerjaan;
    data['hp'] = hp;
    data['alamat'] = alamat;
    data['pendidikan'] = pendidikan;

    console.log(data)
});