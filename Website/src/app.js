angular.module('craneStatic.app', [])
    .controller('craneController', function($http, $scope) {
      var $ctrl = this;
        $ctrl.location = "/py/control/";
        $ctrl.cam = "1";
        $ctrl.speed = 125;
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
        
        $ctrl.platformCW = function() {            
            $ctrl.actionFunction = $ctrl.platformCW;
            $http.get($ctrl.location + "rotation/cw/1/ccw/0/speed/128");
        }

        $ctrl.platformCCW = function() {
            $ctrl.actionFunction = $ctrl.platformCCW;
            $http.get($ctrl.location + "rotation/cw/0/ccw/1/speed/128");
        }

        $ctrl.platformStop = function() {
            $ctrl.actionFunction = $ctrl.platformStop;
            $http.get($ctrl.location + "rotation/cw/0/ccw/0/speed/128");
        }

        $ctrl.updateSpeed = function() {
            if(!!$ctrl.actionFunction)
                $ctrl.actionFunction();
        }

        $ctrl.cameraUp = function() {
            $http.get($ctrl.location + "cam/up");
        }

        $ctrl.cameraCW = function() {
            $http.get($ctrl.location + "cam/cw")
        }

        $ctrl.cameraCCW = function() {
            $http.get($ctrl.location + "cam/ccw")
        }

        $ctrl.cameraDown = function() {
            $http.get($ctrl.location + "cam/down")
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
            $ctrl.actionFunction = null;
        }
    })
    .run(function() {
        console.log("Startup");
    });
