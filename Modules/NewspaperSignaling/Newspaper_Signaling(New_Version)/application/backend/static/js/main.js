function trendAnalysis(event){

    const loadingOverlay = $('#loadingOverlay');
    loadingOverlay.css("display", "flex");
    const title_alarm_system = $('#title-alarm-system');
    title_alarm_system.css("background-color", "rgba(0, 0, 0, 0.01)");
    const title_stat_trend_analysis = $('#title-stat-trend-analysis');
    title_stat_trend_analysis.css("background-color", "rgba(0, 0, 0, 0.01)");
    const title_relevant_keywords = $('#title-relevant-keywords');
    title_relevant_keywords.css("background-color", "rgba(0, 0, 0, 0.01)");


    const timeoutMilliseconds = 3000; // 3 seconds
    setTimeout(function() {

        // Hide loading overlay
        loadingOverlay.css("display", "none");
        title_alarm_system.css("background-color", "white");
        title_stat_trend_analysis.css("background-color", "white");
        title_relevant_keywords.css("background-color", "white");

        var warning_text = $(".warning_text")
        var alert_system_div = $("#alert_system_div")
        var qa_chat_bot = $("#qa_chat_bot")
        var stat_trend_analysis = $("#stat_trend_analysis")
        var relevant_words = $("#relevant_words")
        
        warning_text.css("display", "none");
        alert_system_div.css("display", "block");
        qa_chat_bot.css("display", "block");
        stat_trend_analysis.css("display", "block");
        relevant_words.css("display", "block");
    

    }, timeoutMilliseconds);
    

    var domainSpecificKeyword = $("#domain-specific-keyword").val();
    var specificAlertKeyword = $("#specific-alert-keyword").val();
    var titleValue = $(".selected-flag").attr("title");
    var monthSelect = $("#month-select").val();
    var yeaSelect = $("#year-select").val();

   
}

function qaChatBotAsk(){
    const loadingOverlay = $('#loadingOverlay-2');
    loadingOverlay.css("display", "flex");

    const timeoutMilliseconds = 2400; // 3 seconds
    setTimeout(function() {

        loadingOverlay.css("display", "none");

        var qa_chat_bot_asked = $("#qa_chat_bot_asked")
        
        qa_chat_bot_asked.css("display", "block");
    }, timeoutMilliseconds);

}

document.addEventListener("DOMContentLoaded", function() {
    // Automatically close the flash message after 2-3 seconds (2000-3000 milliseconds)
    setTimeout(function() {
        var flashMessage = document.getElementById("flash-message");
        if (flashMessage) {
            flashMessage.style.display = "none"; // Hide the flash message
        }
    }, 100); // Adjust the timeout as needed (e.g., 3000 for 3 seconds)
});
