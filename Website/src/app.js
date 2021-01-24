angular.module('craneStatic.app', [])
    .controller('craneController', function($http) {
      var $ctrl = this;
        $ctrl.location = "http://localhost/py/control/";
        $ctrl.cam = "1";
        var on = 0;

        $ctrl.platform = function(n, s, e, w) {
            $http.get($ctrl.location + "platform/north/" + n + "/south/" + s + "/east/" + e + "/west/" + w);
        }
        
        $ctrl.hookUp = function() {
            $http.get($ctrl.location + "hook/up/1/down/0");
        }

        $ctrl.hookDown = function() {
            $http.get($ctrl.location + "hook/up/0/down/1");
        }

        $ctrl.hookStop = function() {
            $http.get($ctrl.location + "hook/up/0/down/0");
        }

        $ctrl.boomUp = function() {
            $http.get($ctrl.location + "boom/up/1/down/0");
        }

        $ctrl.boomDown = function () {
            $http.get($ctrl.location + "boom/up/0/down/1");
        }

        $ctrl.boomStop = function () {
            $http.get($ctrl.location + "boom/up/0/down/0");
        }

        $ctrl.toggleRelay = function() {
            if(on == 0)
                on = 1;
            else
                on = 0;
            
            $http.get($ctrl.location + "magnet/" + on);
        }
        
        $ctrl.stop = function() {
            $http.get($ctrl.location + "off");
        }
    })
    .run(function() {
        console.log("Startup");
    });
