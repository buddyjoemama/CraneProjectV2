angular.module('craneStatic.app', [])
    .controller('craneController', function($http) {
      var $ctrl = this;
        $ctrl.location = "http://localhost/py/control/";
        var on = 0;

        $ctrl.action = function(n, s, e) {
            $http.get($ctrl.location + "north/" + n + "/south/" + s + "/extra/" + e);
        }
        
        $ctrl.toggleRelay = function() {
            if(on == 0)
                on = 1;
            else
                on = 0;
            
            $http.get($ctrl.location + "magnet/" + on);
        }
        
        $ctrl.stop = function() {
            $http.get($ctrl.location + "stop");
        }
    })
    .run(function() {
        console.log("Startup");
    });
