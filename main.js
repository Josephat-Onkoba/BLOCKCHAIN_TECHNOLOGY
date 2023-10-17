const SHA256 = require('crypto-js/sha256');

class Block{
    constructor(index, timestamp, data, previousHASH = ""){
        this.index = index;
        this.timestamp = timestamp;
        this.data = data;
        this.previousHASH = previousHASH;
        this.hash = "";
    }

    calculateHash(){
        return SHA256(this.index + this.previousHASH + this.timestamp + JSON.stringify(this.data)).toString();
    }
}

class Blockchain{
    constructor(){
        this.chain = [this.createGenesisBlock()];

    }
    createGenesisBlock(){
        return new Block(0, "01/01/2023", "Genesis Block", "0");
    }
    getLatestBlock(){
        return this.chain[this.chain.length - 1];
    }
    addBlock(newBlock){
        newBlock.previousHASH = this.createGenesisBlock().hash;
        newBlock.hash = newBlock.calculateHash();
        this.chain.push(newBlock)
    }
    isChainValid(){
        for(let i = 1; i < this.chain.length; i++){
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];
            if(currentBlock.hash !== currentBlock.calculateHash()){
                return false;
            }
            if(currentBlock.previousHASH !== previousBlock.hash){
                return false;
            }
        }
        
        return true;
    }
}

let onkobacoin = new Blockchain();
onkobacoin.addBlock(new Block(1, "02/02/2023", {amount: 4}));
onkobacoin.addBlock(new Block(1, "03/03/2023", {amount: 10}));

console.log('is Blockchain Valid? ' + onkobacoin.isChainValid());

//console.log(JSON.stringify(onkobacoin, null, 4));
