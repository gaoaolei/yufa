window.open('freereader://event_statistic?param={"type":"withdraw_pv"}','_self');

// 提现功能
var j_front_withdraw_config = {
    SMCaptcha : '',
    jsVerificationErrorTxtObj : $('.js-verification-error-txt'),
    captchaId : 'js-verification-display-area',
    captcha_rid : '',
    withdrawMoneyObj : $('.js-withdraw-money'),
    withdrawNameObj : $('.js-withdraw-name'),
    configId : '',
    dataType: '',
    jsLoadingObj: $('.js-loading'),
    eventObj:'',
    submitWithdrawData:{},
    rewardVideoData:{},
    bindPhoneTxtObj: $('.js-bind-phone-pop-txt'),
    bindWechatTxtObj: $('.js-bind-wechat-pop-txt'),
    appVersion: 0,
    availableCashMoney: $('.js-available-cash-number').attr('data-available-cash'),
    inviteFriendErrorMoney: '',
    inviteFriendErrorCancelBtn: $('.js-invite-friends-error-cancel-btn'),
    inviteFriendErrorTit: $('.js-invite-friends-error-tit'),
    inviteFriendErrorSubmitBtn: $('.js-invite-friends-error-submit-btn')
}

if(navigator.userAgent.toLowerCase().match(/webviewversion\/(\S*)/)){
    j_front_withdraw_config.appVersion = parseInt(navigator.userAgent.toLowerCase().match(/webviewversion\/(\S*)/)[1]);
}

// 创建数美验证码
initSMCaptcha({
    organization: 'KJNSBIdTWSOiYNEsCLS9', //数美后台查看
    width: '100%'
}, function(instance) {
    j_front_withdraw_config.SMCaptcha = instance;
    j_front_withdraw_config.SMCaptcha.appendTo(j_front_withdraw_config.captchaId);
    j_front_withdraw_config.SMCaptcha.onSuccess(function(data) {
        if (!data.pass) {
            j_front_withdraw_config.jsVerificationErrorTxtObj.text('请控制拼图块对齐缺口');
        } else {
            j_front_withdraw_config.captcha_rid = data.rid;
            j_front_withdraw_config.jsVerificationErrorTxtObj.text('');
            if(j_front_withdraw_config.dataType == 'exchange'){
                if (j_front_withdraw_config.configId != 8) {
                    kmPackageObj.pop().show('submit-exchange-pop');
                    window.open('freereader://event_statistic?param={"type":"withdraw_exchangeconfirmationpage"}','_self');
                } else {
                    $.ajax({
                        type: 'GET',
                        url: '//xiaoshuo.km.com/h5/v1/invite-friend/get-encourage-video',
                        success: function (data) {
                            if(data.code == '1'){
                                kmPackageObj.pop().show('submit-exchange-pop');
                                window.open('freereader://event_statistic?param={"type":"withdraw_exchangeconfirmationpage"}','_self');
                            }else{
                                // 显示激励视频
                                kmPackageObj.pop().show('submit-exchange-encourage-pop');
                                j_front_withdraw_config.rewardVideoData = data.data;
                            }
                        }
                    });
                }
            }else{
                kmPackageObj.pop().show('submit-withdraw-pop');
                window.open('freereader://event_statistic?param={"type":"withdraw_confirmationpage"}','_self');
            }
            
            setTimeout(function(){
                window.open('freereader://enable_slide_x','_self');
            },100)
            setTimeout(function(){
                window.open('freereader://enable_web_swipe_refresh','_self');
            },200)
        }
    })
    j_front_withdraw_config.SMCaptcha.onError(function(errType, errMsg) {
        // console.log(errType);
        // console.log(errMsg);
        kmPackageObj.toast({
            txt: '账号异常，提现失败<br>有疑问请联系客服'
        })
    })

    $('.js-verification-change-btn').on('click', function() {
        j_front_withdraw_config.SMCaptcha.reset();
    })

    $('.km-pop-hide-btn[km-pop-name=verification-submit-pop],.km-pop-mask').on('click',function(){
        window.open('freereader://enable_slide_x','_self');
        setTimeout(function(){
            window.open('freereader://enable_web_swipe_refresh','_self');
        },100)
    })

});


// 提现验证码
function verificationWithdraw(){
    if(j_front_withdraw_config.dataType == 'exchange'){
        j_front_withdraw_config.submitWithdrawData = { congif_id: j_front_withdraw_config.configId, data_type: 1 }
    }else{
        j_front_withdraw_config.submitWithdrawData = { congif_id: j_front_withdraw_config.configId}
    }
    $.ajax({
        type: 'POST',
        url: '//xiaoshuo.km.com/h5/v1/invite-friend/withdraw-pre-apply',
        data: j_front_withdraw_config.submitWithdrawData,
        dataType: 'json',
        success: function(data){
            j_fun_forced_upgrade(data);
            j_fun_wake_login(data);
            j_front_withdraw_config.jsLoadingObj.css('display','');
            if(data.errors != undefined){
                if(data.errors.code == 44010107 ){
                    if(j_front_withdraw_config.dataType == 'exchange'){
                        j_front_withdraw_config.bindPhoneTxtObj.text('绑定后才可兑换提现哟~');
                    }else{
                        j_front_withdraw_config.bindPhoneTxtObj.text('绑定后才可以提现哟');
                    }
                    kmPackageObj.pop().show('bind-phone-pop');
                    window.open('freereader://event_statistic?param={"type":"withdraw_phone"}','_self');
                }else if(data.errors.code == 44010106 ){
                    if(j_front_withdraw_config.dataType == 'exchange'){
                        j_front_withdraw_config.bindWechatTxtObj.text('绑定后将兑换提现至该微信');
                    }else{
                        j_front_withdraw_config.bindWechatTxtObj.text('绑定后将提现至该微信');
                    }
                    kmPackageObj.pop().show('bind-wechat-pop');
                    window.open('freereader://event_statistic?param={"type":"withdraw_wechat"}','_self');
                }else if (data.errors.code == 13101005) {
                    kmPackageObj.pop().show('one-yuan-withdraw-error-pop');
                    window.open('freereader://event_statistic?param={"type":"withdraw_withdraw1_readtask"}', '_self');
                }else if (data.errors.code == 99101002) {
                    setInviteFriendErrorPopData(data);
                }else{
                    kmPackageObj.pop().hide();
                    kmPackageObj.toast({
                        tit: data.errors.title
                    })
                }
            }else{
                if(data.status == 0){
                    j_front_withdraw_config.SMCaptcha.reset();
                    j_front_withdraw_config.withdrawMoneyObj.text(data.data.amount);
                    j_front_withdraw_config.withdrawNameObj.text(data.data.weixin_name);
                    kmPackageObj.pop().show('verification-submit-pop');
                    window.open('freereader://disable_slide_x','_self');
                    setTimeout(function(){
                        window.open('freereader://disable_web_swipe_refresh','_self');
                    },100)
                }else{
                    kmPackageObj.pop().hide();
                    kmPackageObj.toast({
                        tit: data.message
                    })
                }
            }
            j_front_withdraw_config.eventObj.attr('click_num', 0);
            
        },
        error: function(xhr, type){
            kmPackageObj.toast({
                tit: '数据请求失败，请稍后重试'
            })
            j_front_withdraw_config.eventObj.attr('click_num', 0);
        }
    })
}

// 确认提现
function submitWithdraw(){
    if(j_front_withdraw_config.dataType == 'exchange'){
        j_front_withdraw_config.submitWithdrawData = { congif_id: j_front_withdraw_config.configId, rid: j_front_withdraw_config.captcha_rid, data_type: 1 }
    }else{
        j_front_withdraw_config.submitWithdrawData = { congif_id: j_front_withdraw_config.configId, rid: j_front_withdraw_config.captcha_rid}
    }
    $.ajax({
        type: 'POST',
        url: '//xiaoshuo.km.com/h5/v1/invite-friend/withdraw-apply',
        data: j_front_withdraw_config.submitWithdrawData,
        dataType: 'json',
        success: function(data){
            j_fun_forced_upgrade(data);
            j_fun_wake_login(data);
            j_front_withdraw_config.jsLoadingObj.css('display','');
            if(data.errors != undefined){
                kmPackageObj.pop().hide();
                if(data.errors.code == 13101015){
                    kmPackageObj.pop().show('withdraw-error-tips-pop');
                }else{
                    kmPackageObj.toast({
                        tit: data.errors.title
                    })
                }
                
            }else{
                if(data.status == 0){
                    if(j_front_withdraw_config.dataType == 'exchange'){
                        if(data.auto == 1){
                            kmPackageObj.pop().show('confirm-auto-exchange-pop');
                        }else{
                            kmPackageObj.pop().show('confirm-exchange-pop');
                        }
                        window.open('freereader://event_statistic?param={"type":"withdraw_exchangeapplicationpage"}','_self');
                    }else{
                        if(data.auto == 1){
                            kmPackageObj.pop().show('confirm-auto-withdraw-pop');
                        }else{
                            kmPackageObj.pop().show('confirm-withdraw-pop');
                        }
                        window.open('freereader://event_statistic?param={"type":"withdraw_applicationpage"}','_self');
                    }
                    j_front_withdraw_config.eventObj.attr('click_num', 1);
                }
            }
            j_front_withdraw_config.eventObj.attr('click_num', 0);
        },
        error: function(xhr, type){
            kmPackageObj.toast({
                tit: '数据请求失败，请稍后重试'
            })
            j_front_withdraw_config.eventObj.attr('click_num', 0);
        }
    })
}

function setInviteFriendErrorPopData(data){
    j_front_withdraw_config.inviteFriendErrorTit.text(data.errors.title);
    j_front_withdraw_config.inviteFriendErrorCancelBtn.attr('data-event-statistic','withdraw_withdraw_' + j_front_withdraw_config.inviteFriendErrorMoney + '_invitationalert_cancel'),
    j_front_withdraw_config.inviteFriendErrorSubmitBtn.attr('data-event-statistic','withdraw_withdraw_' + j_front_withdraw_config.inviteFriendErrorMoney + '_invitationalert_invite'),
    kmPackageObj.pop().show('invite-friends-error-pop');
    window.open('freereader://event_statistic?param={"type":"withdraw_withdraw_' + j_front_withdraw_config.inviteFriendErrorMoney + '_invitationalert"}', '_self');
}

// 可提现按钮
$('.js-withdraw-btn:not([disabled]),.js-one-yuan-withdraw-btn').on('click',function(){
    if(!$(this).attr('click_num') || $(this).attr('click_num') == 0){
        $(this).attr('click_num', 1);
        j_front_withdraw_config.configId = $(this).attr('config_id');
        j_front_withdraw_config.eventObj = $(this);
        j_front_withdraw_config.dataType = $(this).attr('data-type');
        j_front_withdraw_config.inviteFriendErrorMoney = $(this).attr('data-money');
        if(j_front_withdraw_config.availableCashMoney < 1 && $(this).hasClass('js-one-yuan-withdraw-btn')){
            kmPackageObj.toast({
                tit: '余额不足，快去邀请赚钱吧~'
            })
            $(this).attr('click_num', 0);
            return false;
        }
        verificationWithdraw();
    }else{
        $(this).attr('click_num', $(this).attr('click_num') + 1);
    }
})

// 不可提现按钮
$('.js-withdraw-btn[disabled][data-type]').on('click',function(){
    if($(this).attr('data-type') == 'invite-cash'){
        // if($(this).attr('config_id') == 1){
        //     kmPackageObj.pop().show('one-yuan-withdraw-error-pop');
        //     window.open('freereader://event_statistic?param={type=withdraw_withdraw1_readtask}','_self');
        // }else{
        //     kmPackageObj.toast({
        //         tit: '余额不足，快去邀请赚钱吧~'
        //     })
        // }
        kmPackageObj.toast({
            tit: '余额不足，快去邀请赚钱吧~'
        })
        
    }else if($(this).attr('data-type') == 'exchange'){
        kmPackageObj.toast({
            tit: '金币不足，快去赚金币吧~'
        })
    }
})


$('a[href*="freereader://settings_bindwechat"]').on('click',function(){
    j_front_withdraw_config.jsLoadingObj.css('display','block');
})

// 提交提现按钮
$('.js-submit-withdraw-btn,.js-submit-exchange-btn').on('click',function(){
    if(!$(this).attr('click_num') || $(this).attr('click_num') == 0){
        $(this).attr('click_num', 1);
        j_front_withdraw_config.eventObj = $(this);
        submitWithdraw();
    }else{
        $(this).attr('click_num', $(this).attr('click_num') + 1);
    }
    
})

$('.js-submit-exchange-encourage-btn').on('click',function(){
    var _list = '';
    j_front_withdraw_config.rewardVideoData.forEach( function(n,i){
        if(i == 0){
            _list += '{"advertiser":"' + n.advertiser + '","appid":"' + n.appid + '","placementId":"' +  n.adv_code + '","type":"oneyuan_coin"}';
        }else{
            _list += ',{"advertiser":"' + n.advertiser + '","appid":"' + n.appid + '","placementId":"' +  n.adv_code + '","type":"oneyuan_coin"}';
        }
    })
    window.open('freereader://watch_reward_video?param={"data":{"content":"","call_back":"watch_reward_video_end_callback","list":[' + _list + ']}}','_self');
    
})

// 确认提现按钮
$('.js-confirm-withdraw-pop-btn,.js-confirm-exchange-pop-btn').on('click',function(){
    if(j_front_withdraw_config.appVersion >= 10105 || j_front_withdraw_config.appVersion == 0){
        window.open('freereader://request_notification','_self');
        setTimeout(function(){
            window.open('freereader://refresh_webview','_self');
        },200)
    }else{
        window.location.reload();
    }
})

// 提现绑定微信回调
function withdraw_bind_wechat_callback(status){
    j_front_withdraw_config.jsLoadingObj.css('display','');
    if(parseInt(status) == 1){
        verificationWithdraw();
    }else{
        window.open('freereader://event_statistic?param={"type":"withdraw_wechat_fail"}','_self');
    }
}

// 提现绑定手机回调
function withdraw_bind_phone_callback(status){
    j_front_withdraw_config.jsLoadingObj.css('display','');
    if(parseInt(status) == 1){
        verificationWithdraw();
    }
}
// 提现功能

// 观看激励视频完回调
function watch_reward_video_end_callback(){
    j_front_withdraw_config.jsLoadingObj.css('display','');
    window.open('freereader://event_statistic?param={"type":"withdraw_watchvideos_complete"}','_self');
    submitWithdraw();
}