for i in `seq 20000`; do
    screen -dmS positionerIOC /dls_sw/work/R3.14.11/support/positioner/iocs/example/bin/linux-x86/stexample.sh
    sleep 10
    if [ 0 -ne $(caget -t -n TESTPOS:MP:INPOS.SEVR) ]; then
        echo "It went wrong..."
        break
    fi
    screen -S positionerIOC -X quit
    sleep 5
done
    
