function enviarMensagemWhatsApp(tipo) {
    let numero = "5521978853576";
    let mensagem = "";


    if (tipo === "solicitar") {
        mensagem = "Olá! Gostaria de saber mais sobre os serviços disponíveis na Care e Afeto.";
    } else if (tipo === "trabalhar") {
        mensagem = "Olá! Tenho interesse em me tornar um cuidador na Care e Afeto.";
    }

    let url = `https://wa.me/${numero}?text=${encodeURIComponent(mensagem)}`;
    window.open(url, "_blank");
}
