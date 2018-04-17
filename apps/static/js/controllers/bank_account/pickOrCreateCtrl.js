app.controller("bankAccountPickOrCreateCtrl", function ($scope, $http, $window, $rootScope) {
    var vm = this;
    vm.url = $rootScope.url;
    vm.accountId = "";
    vm.accounts = [];
    vm.selectBank = "";
    vm.bankChoices = [
        {
            "value": -1,
            "display_name": "Others"
        },
        {
            "value": 0,
            "display_name": "BBL"
        },
        {
            "value": 1,
            "display_name": "Kbank"
        },
        {
            "value": 2,
            "display_name": "Scb"
        },
        {
            "value": 3,
            "display_name": "Ktb"
        },
        {
            "value": 4,
            "display_name": "Tmb"
        },
        {
            "value": 5,
            "display_name": "Krungsri"
        },
        {
            "value": 6,
            "display_name": "Tanachart"
        },
        {
            "value": 7,
            "display_name": "Uob"
        },
        {
            "value": 8,
            "display_name": "Tisco"
        },
        {
            "value": 9,
            "display_name": "Lh"
        },
        {
            "value": 10,
            "display_name": "Cimb"
        },
        {
            "value": 11,
            "display_name": "Gsb"
        }
    ];
    vm.selectedBanking = vm.bankChoices[0];
    vm.bankTypeChoices = [
                    {
                        "value": 0,
                        "display_name": "Visa"
                    },
                    {
                        "value": 1,
                        "display_name": "Mastercard"
                    }
                ];
    vm.selectedBankType = vm.bankTypeChoices[0];
    vm.addCardBoolean = false;

    vm.getAccountId = function (accountId) {
        vm.accountId = accountId;
    };

    vm.getBankAccounts = function () {
        $http.get(vm.url + '/api/bank_accounts/?account_owner=' + vm.accountId).then(
            function success(response) {
                vm.accounts = response.data;
                vm.selectBank = vm.accounts.findIndex(function (account) {
                    return account.is_primary === true;
                });
                console.log(vm.selectBank);
            },
            function failure() {
                alert("Failed");
            }
        )
    };
    vm.getBankAccounts();
    vm.updateSelectedBank = function (index) {
        vm.selectBank = index;
    };

    vm.delBank = function (index) {
        vm.accounts.splice(index, 1);
    };
    vm.addCard = function () {
        vm.addCardBoolean = true;
    };
    vm.saveNewBankAccount = function () {
        var data = {
            bank: vm.selectBank.value,
            account_number: vm.accountNumber,
            promptpay_phone_number: vm.promptpayPhoneNumber,
            promptpay_citizen_id: vm.promptpayCitizenId,
            card_type: vm.selectedBankType.value,
            is_active: true,
            is_primary: true,
            account_owner: vm.accountId
        };
        $http.post(vm.url + '/api/bank_accounts/', data).then(
            function success() {
                vm.getBankAccounts();
            },
            function fail(response) {
                alert("failed");
            }
        )
    };
    $scope.updateSelectedAccount = function (accountId) {
        $scope.selectedAccount = accountId;
    };

    vm.updatePrimaryAccount = function () {

        var accountId = vm.accounts[vm.selectBank].id;
        var data = {
            primary: true
        };
        $http.patch(vm.url + '/api/bank_accounts/' + accountId + '/', data).then(
            function (response) {
                console.log(response);
                alert('success');
                $window.location.href =  vm.url + '/order/place_order/';
            },
            function (response) {
                console.log(response);
                alert('failed');
            }
        );
    };

    vm.nextPage = function () {
        if ($scope.selectedAccount === "") {
            alert("pls select choose or add a card");
            return;
        }
        vm.updatePrimaryAccount();
    };

    vm.nextForPaymentSlip = function () {
        $window.location.href =  vm.url + '/order/place_order/';
    };
});