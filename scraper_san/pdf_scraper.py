
    def forward(self, idx, targets=None):
        # Pack the input sequences
        packed_idx = rnn_utils.pack_sequence(idx, enforce_sorted=False)

        # Forward pass through the model
        tok_emb = self.token_embedding_table(packed_idx.data)
        pos_emb = self.position_embedding_table(torch.arange(tok_emb.size(0), device=device))
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        # Unpack the output
        logits = rnn_utils.pad_packed_sequence(rnn_utils.PackedSequence(logits, packed_idx.batch_sizes))[0]

        if targets is None:
            loss = None
        else:
            targets = rnn_utils.pad_sequence(targets, batch_first=True)
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)

        return logits, loss