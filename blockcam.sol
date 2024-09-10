// SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.9;

contract CCTV {
    struct Admin {
        string userName;
        address adminAddress;
    }

    struct Video {
        string videoClip;
        uint timeStamp;
    }

    address payable public owner;
    Admin[] private adminData;
    mapping(address => Video[]) private adminVideos;

    constructor() {
        owner = payable(msg.sender);
    }

    function registerAdmin(string memory _name) public payable {
        // require(msg.value > 0, "Please pay some ether");
        owner.transfer(msg.value);
        adminData.push(Admin(_name, msg.sender));
    }

    function addData(string memory videoLink) public payable  {
        bool isAdmin = false;
        for (uint i = 0; i < adminData.length; i++) {
            if (adminData[i].adminAddress == msg.sender) {
                isAdmin = true;
                break;
            }
        }
        require(isAdmin, "Only registered admins can add data");
        adminVideos[msg.sender].push(Video(videoLink, block.timestamp));
    }

    function viewData() public view returns (Video[] memory) {
        return adminVideos[msg.sender];
    }

    function getAdminDetails() public view returns (Admin[] memory) {
        return adminData;
    }
}