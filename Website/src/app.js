angular.module('craneStatic.app', [])
    .controller('craneController', function($http, $scope) {
      var $ctrl = this;
        $ctrl.location = "http://localhost/py/control/";
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
            $http.get($ctrl.location + "rotation/cw/1/ccw/0/speed/" + $ctrl.speed);
        }

        $ctrl.platformCCW = function() {
            $ctrl.actionFunction = $ctrl.platformCCW;
            $http.get($ctrl.location + "rotation/cw/0/ccw/1/speed/" + $ctrl.speed);
        }

        $ctrl.updateSpeed = function() {
            $ctrl.actionFunction();
        }

        $ctrl.cameraUp = function() {
            $http.get($ctrl.location + "cam/cw");
        }

        $ctrl.cameraCW = function() {
            $http.get($ctrl.location + "cam/down")
        }

        $ctrl.cameraCCW = function() {
            $http.get($ctrl.location + "cam/up")
        }

        $ctrl.cameraDown = function() {
            $http.get($ctrl.location + "cam/ccw")
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
