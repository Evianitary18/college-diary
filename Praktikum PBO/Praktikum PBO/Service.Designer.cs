namespace Praktikum_PBO
{
    partial class Service
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            dataGridView1 = new DataGridView();
            Colunm1 = new DataGridViewTextBoxColumn();
            Column2 = new DataGridViewTextBoxColumn();
            Column3 = new DataGridViewTextBoxColumn();
            button = new Button();
            numericUpDown1 = new NumericUpDown();
            button1 = new Button();
            button2 = new Button();
            Column4 = new DataGridViewTextBoxColumn();
            Column1 = new DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).BeginInit();
            SuspendLayout();
            // 
            // dataGridView1
            // 
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Columns.AddRange(new DataGridViewColumn[] { Colunm1, Column2, Column3, Column4, Column1 });
            dataGridView1.Location = new Point(12, 153);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.RowTemplate.Height = 25;
            dataGridView1.Size = new Size(776, 150);
            dataGridView1.TabIndex = 0;
            dataGridView1.CellContentClick += dataGridView1_CellContentClick;
            // 
            // Colunm1
            // 
            Colunm1.HeaderText = "ID";
            Colunm1.Name = "Colunm1";
            // 
            // Column2
            // 
            Column2.HeaderText = "Deposit";
            Column2.Name = "Column2";
            // 
            // Column3
            // 
            Column3.HeaderText = "Kolom3";
            Column3.Name = "Column3";
            // 
            // button
            // 
            button.Location = new Point(133, 49);
            button.Name = "button";
            button.Size = new Size(75, 23);
            button.TabIndex = 1;
            button.Text = "deposit";
            button.UseVisualStyleBackColor = true;
            button.Click += deposit_Click;
            // 
            // numericUpDown1
            // 
            numericUpDown1.Location = new Point(7, 49);
            numericUpDown1.Name = "numericUpDown1";
            numericUpDown1.Size = new Size(120, 23);
            numericUpDown1.TabIndex = 2;
            // 
            // button1
            // 
            button1.Location = new Point(214, 49);
            button1.Name = "button1";
            button1.Size = new Size(75, 23);
            button1.TabIndex = 3;
            button1.Text = "tambah rp.";
            button1.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            button2.Location = new Point(295, 49);
            button2.Name = "button2";
            button2.Size = new Size(75, 23);
            button2.TabIndex = 4;
            button2.Text = "delete first";
            button2.UseVisualStyleBackColor = true;
            // 
            // Column4
            // 
            Column4.HeaderText = "Update";
            Column4.Name = "Column4";
            // 
            // Column1
            // 
            Column1.HeaderText = "Delete";
            Column1.Name = "Column1";
            // 
            // Service
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(numericUpDown1);
            Controls.Add(button);
            Controls.Add(dataGridView1);
            Name = "Service";
            Text = "Service";
            Load += Service_Load;
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private DataGridView dataGridView1;
        private DataGridViewTextBoxColumn Colunm1;
        private DataGridViewTextBoxColumn Column2;
        private DataGridViewTextBoxColumn Column3;
        private Button button;
        private NumericUpDown numericUpDown1;
        private Button button1;
        private Button button2;
        private DataGridViewTextBoxColumn Column4;
        private DataGridViewTextBoxColumn Column1;
    }
}