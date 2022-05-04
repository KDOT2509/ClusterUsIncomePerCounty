// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
pragma abicoder v2;

contract UsIncome{
    // Declaring variables
    // address public FederalGovernment = 0x86D15B422D924D9115986Dd7A87ee794CAF2cbaF;
    mapping (address => bool) public stateWallets;
    mapping (uint => incomeData) public stateIdToIncomeData;
    uint public entryID = 0;

    struct incomeData{
        string stateName;
        string countyName;
        uint perCapitaIncome2018;
        uint perCapitaIncome2019;
        uint perCapitaIncome2020;
    }

    // modifier isFederalGovernment() {
    //     require(msg.sender == FederalGovernment);
    //     _;
    // }

    function reportCountyIncome(
        string memory _stateName,
        string memory _countyName,
        uint _perCapitaIncome2018,
        uint _perCapitaIncome2019,
        uint _perCapitaIncome2020
        ) public {
            uint entryID = entryID++;
            stateIdToIncomeData[entryID] = incomeData( _countyName, _stateName, _perCapitaIncome2018, _perCapitaIncome2019, _perCapitaIncome2020);
    }

    function getIncomeData() public view returns (incomeData[] memory) {
        incomeData [] memory memoryArray = new incomeData[](entryID);
        for(uint i = 0; i < entryID; i++) {
            memoryArray[i] = stateIdToIncomeData[i];
        }
        return memoryArray;
    }

    // function getStateIncomeData() public view returns(incomeData[] memory) {

    // }
    
    // MyStruct[] myStructArray;

    function getStateIncomeData(string memory _stateName) public view returns(incomeData[] memory){ // change on what you need to return
        incomeData [] memory memoryArrayState = new incomeData[](entryID);
 // change on what you need to return

        for(uint i = 0; i<entryID; i++){
            if (keccak256(abi.encodePacked(stateIdToIncomeData[i].stateName)) == keccak256(abi.encodePacked(_stateName))){
                memoryArrayState[i]=stateIdToIncomeData[i]; //or whatever you want to do if it matches
            }
        }
        return memoryArrayState;
    }    

    // MyStruct[] myStructArray;

    // function checkArray() constant returns(bool[]){ // change on what you need to return
    //     bool[] checker; // change on what you need to return

    //     for(uint i = 0; i<myStructArray.length; i++){
    //         if(myStructArray[i].foo == bar){
    //             checker[i]=true; //or whatever you want to do if it matches
    //         }
    //         else{
    //             checker[i]=false;
    //         }
    //     }
    //     return checker;
    // }
}   