// ROTAS PARA RETORNO DOS VALORES PARA O DASHBOARD

// INPUTS
$(document).ready(function() {
    $.get('http://localhost:5000/values-info', function(data) {
    $('#total_input').text(data.inputs);            // INPUTS
    $('#total_base').text(data.total);              // TOTAL
    $('#total_ativo').text(data.ativo);             // ATIVO
    $('#target_ativo').text(data.inputs);           // EM ANÁLISE
    $('#total_lgpd').text(data.lgpd);               // LGPD
    $('#target_lgpd').text(data.inputs);            // INPUTS
    $('#total_resp').text(data.limresp);            // RESP
    $('#target_resp').text(data.inputs);            // INPUTS
    });
});

// CHARTS
$(document).ready(function() {
    $.get('http://localhost:5000/chart-values', function(data) {
        // CHART 1
        $('#chart_1_1_p').css({"stroke-dashoffset": String(data.total_analise_pg)}); // COMPLETUDE - ANALISE
        $('#chart_1_2_p').css({"stroke-dashoffset": String(data.total_ativo_pg)}); // COMPLETUDE - ATIVO
        $('#chart-1-1_abs').text(String(data.total_analise_abs) + "%"); // LGPD - TRUE

        // CHART 3
        $('#chart_3_1_p').css({"stroke-dashoffset": String(data.total_lgpd_pg)}); // LGPD - TRUE
        $('#chart_3_1_abs').text(String(data.total_lgpd_abs) + "%"); // LGPD - TRUE
        
        // CHART 4
        $('#chart_4_1_p').css({"stroke-dashoffset": String(data.total_resp_pg)}); // RESP - TRUE
        $('#chart_4_1_abs').text(String(data.total_resp_abs) + "%"); // RESP - TRUE
    });
});